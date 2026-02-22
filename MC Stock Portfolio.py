import pandas as pd 
import numpy as np 
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf

#========================================================
# loading the data
#========================================================
def get_data(stock_list, start, end): 
    stock_data = yf.download(stock_list, start, end)    # Returns a pd.dataframe for open, high, low, close, adj close, volume. 
    stock_data = stock_data["Close"]                    # Return only "Close" Series
    pct_returns = stock_data.pct_change().dropna()      # Calculates daily percent returns
    mean_returns = pct_returns.mean()                   # Returns the aggregated daily mean of each Stock
    cov_matrix = pct_returns.cov()                      # Returns the daily cov matrix that will show how each stock affects the portfolio overall
    return mean_returns, cov_matrix


# Your "stock portfolio", indexes might require different naming conventions
stock_list = ['TSM', 'AAPL', 'NVDA', 'AMZN', 'SPY', 'QQQ', '^N225', 'TSLA'] 

end_date = dt.datetime.now()                            
start_date = end_date - dt.timedelta(days=300)     #limit the dataset to 300 days, standard for a short term, better reflects current risk but unstable

mean_returns, cov_matrix = get_data(stock_list, start_date, end_date)

print(mean_returns)                          

# Defining weights for the portfolio, essentially how much this particular stock will affect the portfolio. 
# Weights we set are randomly assigned to each stock
weights = np.random.random(len(mean_returns)) 
weights /= np.sum(weights) 

#======================================================
# Monte Carlo Method
#======================================================

number_of_sims = 100000     #choose the number of simulations
time_days = 100             #timeframe in days

n_assets = len(weights)                                                         
meanM = np.full( shape=(time_days, n_assets), fill_value= mean_returns)         # we create a matrix to store our "mean_returns" vector, to later apply "shocks" 

portfolio_sims = np.zeros( (time_days, number_of_sims) )                        # After simulating shocks to our meanM, we hold the new float values here

initial_portfolio_value = 10000

for m in range(0, number_of_sims):                                                                  
    # MC loops 
    Z = np.random.normal( size=(time_days, n_assets) )                          # random uncorrelated variables from a normal dist. for the simulated parts (independent shocks)
    L = np.linalg.cholesky(cov_matrix)                                          # using cholesky decoposition, we find the lower trianular matrix of the daily_cov_matrix Shape =(n_assets, n_assets)
    correlated_shocks = np.matmul( Z, L.T )                                     # matrix multiply to combine to create correlated shocks
    daily_returns = meanM + correlated_shocks 
    portfolio_returns= np.matmul(weights, daily_returns.T)
    portfolio_path = initial_portfolio_value * np.cumprod(1+ portfolio_returns)                          
    portfolio_sims[:,m] = portfolio_path                                        # here the dailyreturns affected by the weights are calculated per day, and accumulated to simulate trends overtime instead


def mcVaR(returns, alpha=5): 
    """
    Input: pandas series of returns
    Output: percentile on return distribution to a given confidence level alpha
    """
    if isinstance(returns, pd.Series): 
        return np.percentile(returns,alpha)
    else: 
        raise TypeError("Expected a pandas data series.")

def mcCVaR(returns, alpha=5): 
    """
    Input: panda series of returns 
    Output: CVaR or Expected Shortfall to a given confidence level alpha
    """
    if isinstance(returns, pd.Series): 
        belowVaR = returns <= mcVaR(returns, alpha=alpha)
        return returns[belowVaR].mean() 
    else: 
        raise TypeError("Expected a pandas data series.")

# ============================================
# Prepare Returns for Risk Metrics
# ============================================
# final portfolio values from all simulations
ending_values = portfolio_sims[-1, :]

#convert returns
returns = (ending_values - initial_portfolio_value) / initial_portfolio_value

# Convert to series
return_series = pd.Series(returns)

weights_df = {
    "Asset": stock_list, 
    "Weight": weights
}

print(weights_df)
# ============================================
# VaR & CVaR Calculations
# ============================================
VaR = mcVaR(return_series, alpha=5)
CVaR = mcCVaR(return_series, alpha=5)
sharpe = return_series.mean() / return_series.std()

# Summary
print(f"\nSharpe Ratio: {sharpe:.4f}")
print(f"Mean Return: {return_series.mean():.2%}")
print(f"VaR (95%): {VaR:.2%}")
print(f"CVaR (95%): {CVaR:.2%}")
print(f"Worst Return: {return_series.min():.2%}")
print(f"Best Return: {return_series.max():.2%}")

#======================================================
# Statistics: mean path and confidence intervals
#======================================================
# used the simulated path for 
# simulated_path = pd.Series(portfolio_sims[:, 0])
mean_path = portfolio_sims.mean(axis=1)


p5 = np.percentile(portfolio_sims, 5, axis=1)
p95 = np.percentile(portfolio_sims, 95, axis=1)

# ============================================
# Drawdown Calculation (Mean Path)
# ============================================
portfolio_series = pd.Series(mean_path)

# running max
running_max = portfolio_series.cummax()

# drawdown
drawdown = (portfolio_series - running_max) / running_max

drawdown_df = pd.DataFrame({
    "Day": range(time_days),
    "Drawdown": drawdown
})

# ============================================
# Export for Power BI
# ============================================

# Export Returns
results_df = pd.DataFrame({
    "Final Portfolio Value": ending_values,
    "Return": returns
})
results_df.to_csv("monte_carlo_results.csv", index=False)

# Export Summary
summary_df = pd.DataFrame({
    "Day": range(time_days),
    "Mean": mean_path,
    "P5": p5,
    "P95": p95
})
summary_df.to_csv("simulation_summary.csv", index=False)

# Export Drawdown
drawdown_df = pd.DataFrame({
    "Day": range(time_days),
    "Drawdown": drawdown
})
drawdown_df.to_csv("drawdown.csv", index=False)


#======================================================
# Plotting
#======================================================
sample_paths = portfolio_sims[:, :100]

fig, ax = plt.subplots(figsize=(12,7))

# Plot fewer simulations (cleaner)
ax.plot(sample_paths, color="gray", alpha=0.08)

# Mean path
ax.plot(mean_path, color="blue", linewidth=3, label="Average Path")

# Confidence interval
ax.fill_between(range(time_days), p5, p95, 
                color="blue", alpha=0.2, label="5–95% CI")
ax.plot(p5, linestyle="--", color="red", alpha=0.7, label="Downside (5%)")

# Baseline
ax.axhline(initial_portfolio_value, linestyle="--", color="black", alpha=0.6)

# Labels & title
ax.set_ylabel("Portfolio Value ($)")
ax.set_xlabel("Time (Days)")
ax.set_title("Monte Carlo Simulation of a Stock Portfolio", fontsize=14)

# Style
ax.grid(alpha=0.3)
ax.legend()

plt.tight_layout()
plt.show()

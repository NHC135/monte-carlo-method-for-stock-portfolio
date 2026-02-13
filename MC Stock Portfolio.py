import pandas as pd 
import numpy as np 
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf

#========================================================
# loading the data
#========================================================
def get_data(stock_data, start, end): 
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

number_of_sims = 100        #choose the number of simulations
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

#======================================================
# Plotting
#======================================================
plt.plot(portfolio_sims)
plt.ylabel("Portfolio Value ($)")
plt.xlabel("Time in days")
plt.title("Monte Carlo Simulation of a stock Portfolio")
plt.show()
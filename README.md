
# 📊 Monte Carlo Portfolio Risk Analysis

## 🚀 Overview

This project implements a **Monte Carlo simulation framework** to model the stochastic behavior of a multi-asset portfolio and evaluate financial risk under uncertainty.

By simulating **100,000+ correlated portfolio paths**, the model estimates return distributions and key risk metrics such as **Value-at-Risk (VaR)** and **Conditional Value-at-Risk (CVaR)**.

The results are visualized through interactive dashboards to provide **data-driven insights into portfolio performance, downside risk, and uncertainty over time**.

---

## 🧠 Key Features

* 📈 Simulates **100,000+ portfolio scenarios** over a 100-day horizon
* 🔗 Models **correlated asset returns** using Cholesky decomposition
* ⚖️ Computes key risk metrics:

  * Value-at-Risk (VaR)
  * Conditional Value-at-Risk (CVaR)
  * Sharpe Ratio
* 📊 Generates:

  * Return distributions
  * Confidence intervals (5th–95th percentile)
  * Portfolio growth projections
  * Drawdown analysis
* 📁 Exports structured datasets for **Power BI visualization**

---

## 🏗️ Methodology

### 1. Data Collection

* Historical price data is retrieved using `yfinance`
* Daily returns, mean returns, and covariance matrix are computed

### 2. Monte Carlo Simulation

* Random shocks are generated from a **normal distribution**
* Cholesky decomposition is applied to introduce **correlation between assets**
* Portfolio returns are simulated over time using weighted assets
* Portfolio value evolves using **geometric compounding**

### 3. Risk Modeling

* **VaR (95%)**: Estimates the worst expected loss under normal conditions
* **CVaR (95%)**: Measures expected loss in extreme scenarios
* **Sharpe Ratio**: Evaluates risk-adjusted performance

---

## 📊 Sample Insights

* 📈 Positive expected return with strong upside potential
* ⚠️ Tail risk identified through CVaR and worst-case outcomes
* 🔄 Portfolio exhibits **positive skew** (more upside than downside)
* 📉 Drawdowns are infrequent but occur in **clusters during stress periods**

---

## 📁 Project Structure

```
.
├── monte_carlo_simulation.py
├── monte_carlo_results.csv
├── simulation_summary.csv
├── drawdown.csv
├── README.md
```

---

## 📤 Outputs

The simulation generates the following datasets:

* **monte_carlo_results.csv**

  * Final portfolio values and returns for all simulations

* **simulation_summary.csv**

  * Mean path and confidence intervals over time

* **drawdown.csv**

  * Portfolio drawdown over the simulation horizon

These outputs are used to build **Power BI dashboards** for visualization.

---

## 📊 Visualization

The model produces:

* Portfolio growth projections with confidence bands
* Distribution of final portfolio values
* Drawdown analysis
* Risk metric summaries

---

## 🛠️ Tech Stack

* **Python**: NumPy, Pandas, Matplotlib
* **Finance/Data**: yfinance
* **Visualization**: Power BI

---

## ⚠️ Assumptions & Limitations

* Asset returns are assumed to follow a **multivariate normal distribution**
* Does not account for:

  * Fat tails (extreme market events)
  * Time-varying volatility
  * Transaction costs

---

## 🚀 Future Improvements

* Implement **fat-tailed distributions (t-distribution)**
* Add **GARCH models** for volatility clustering
* Portfolio optimization (efficient frontier, Sharpe maximization)
* Stress testing (market crash scenarios)

---

## 💡 Key Takeaway

This project demonstrates how Monte Carlo simulation can be used to:

> Quantify uncertainty, evaluate downside risk, and model the probabilistic behavior of investment portfolios.

---

## 👤 Author

**Nathaniel Hwan Choi**

* GitHub: https://github.com/NHC135
* LinkedIn: https://www.linkedin.com/in/nathaniel-choi-0b2981148

---

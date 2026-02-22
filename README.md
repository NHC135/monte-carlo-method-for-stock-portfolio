# 📈 Monte Carlo Simulation for **Stock Portfolio Risk Analysis**

This project applies the **Monte Carlo simulation method** to model the **uncertainty and variability** of a diversified stock portfolio.  
It uses **historical data from Yahoo Finance** to estimate **expected returns**, **covariance**, and to **simulate thousands of future portfolio outcomes**.

---

## 🧠 **Key Concepts**

- **Mean-Variance Optimization:** Captures expected returns and covariance between assets.  
- **Monte Carlo Simulation:** Models uncertainty through random sampling of possible returns.  
- **Cholesky Decomposition:** Introduces *correlated random shocks* to mimic realistic market behavior.  
- **Confidence Intervals:** Shows the range of possible portfolio values (5th–95th percentile).  

---

## 🧩 **Project Workflow**

1. **Data Collection**
   - Pulls *daily closing prices* from Yahoo Finance using `yfinance`.  
   - Calculates **daily returns**, **mean returns**, and the **covariance matrix**.  

2. **Portfolio Setup**
   - Defines a portfolio of stocks with **randomly generated weights** that sum to 1.  
   - Assigns an **initial portfolio value** (e.g., \$10,000).  

3. **Monte Carlo Simulation**
   - Runs **10,000 simulations** over a **100-day** period.  
   - Applies **correlated shocks** using **Cholesky decomposition**.  
   - Tracks **daily portfolio growth** over time for each simulated path.  

4. **Visualization**
   - Displays all simulated paths in gray for context.  
   - Highlights the **average portfolio path** in blue.  
   - Shades the **5–95% confidence interval** for risk visualization.  

---

## 🧮 **Mathematical Foundation**  
explanation and intuition can be found in the notion link, as well as the documentation
https://www.notion.so/Monte-Carlo-Simulation-of-a-Stock-Portfolio-in-Python-27e7e74ba6a38099a5bad1cd8f7c045e?source=copy_link
---

## 📊 **Results Visualization**

- Gray lines → All simulated portfolio paths  
- Blue line → **Average portfolio performance**  
- Blue shaded area → **5–95% Confidence Interval**  
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/3d5d2878-beca-45e3-80ca-e4a331157468" />    
  
**updated:**   
<img width="1200" height="700" alt="Figure_1" src="https://github.com/user-attachments/assets/b2ba1572-ea29-4909-a23b-d83dbcc39e3f" />


---

## ⚙️ **Technologies Used**

| Library | Purpose |
|----------|----------|
| **pandas** | Data cleaning and manipulation |
| **numpy** | Numerical computation and random sampling |
| **matplotlib** | Visualization of portfolio simulations |
| **yfinance** | Stock data extraction from Yahoo Finance |
| **datetime** | Managing time periods for data retrieval |

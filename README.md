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
explanation and analysis can be found in the notion link, as well as the documentation  
https://www.notion.so/Monte-Carlo-Simulation-of-a-Stock-Portfolio-in-Python-27e7e74ba6a38099a5bad1cd8f7c045e?source=copy_link
---

## 📊 **Results Visualization**

- Gray lines → All simulated portfolio paths  
- Blue line → **Average portfolio performance**  
- Blue shaded area → **5–95% Confidence Interval**  
<img width="1200" height="700" alt="Figure_1" src="https://github.com/user-attachments/assets/e83f85a7-b069-4630-a02a-1e4de2e2e507" />

## PowerBI Visualizations
<img width="1426" height="804" alt="Screenshot 2026-02-19 212454" src="https://github.com/user-attachments/assets/322b4aa3-41b7-40f4-8d1b-3f248a1143ff" />
<img width="1430" height="801" alt="Screenshot 2026-02-19 212512" src="https://github.com/user-attachments/assets/729cbdcd-08e1-414f-aafb-24ab26a9b832" />


---

## ⚙️ **Technologies Used**

| Library | Purpose |
|----------|----------|
| **pandas** | Data cleaning and manipulation |
| **numpy** | Numerical computation and random sampling |
| **matplotlib** | Visualization of portfolio simulations |
| **yfinance** | Stock data extraction from Yahoo Finance |
| **datetime** | Managing time periods for data retrieval |

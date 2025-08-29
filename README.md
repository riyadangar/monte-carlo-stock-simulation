Monte Carlo Stock Price Simulation

Python simulation estimating stock price paths using volatility &amp; historical returns.

This project uses Monte Carlo simulation in Python to estimate potential stock price pathways and calculate the probability of gains or losses. The model is based on historical volatility and returns, commonly used in quantitative finance and risk analysis.

Features:

- Simulates thousands of possible stock price paths.
- Incorporates historical volatility and expected returns.
- Produces probability distributions of future prices.
- Visualises results using matplotlib.

How It Works:

- Collect historical stock returns data (can be real or sample data).
- Calculate mean daily return and volatility.
- Run a Monte Carlo simulation to generate thousands of possible price paths.
- Plot results and estimate the likelihood of gains/losses.

Example Output:

  typical output plot shows multiple simulated stock price trajectories and a histogram of final prices after the chosen time horizon.

Technologies Used:

- Python
- NumPy, Pandas for data analysis
- Matplotlib for visualisation

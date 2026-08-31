A Python script that simulates possible future stock price paths using Monte Carlo methods, based on a stock's historical volatility and average returns.

It pulls price history for a ticker, works out the average daily return and volatility from that data, then runs thousands of random simulations forward to see where the price could realistically end up. The output is a fan chart of all the simulated paths plus a histogram showing the spread of final prices, along with a rough probability of the price finishing higher than where it started.

This is a simplified model (it assumes returns are normally distributed, which real markets don't perfectly follow), so it's meant for learning and exploring Monte Carlo simulation, not for making actual trading decisions.

To run it, install numpy, pandas, matplotlib, and yfinance, then run the script directly. You can change the ticker, start date, forecast length, and number of simulations by editing the config values near the top of the file. It saves two plots (paths.png and terminal_hist.png) and prints the starting price and probability of a gain to the terminal.

Built with Python, NumPy, Pandas, and Matplotlib.

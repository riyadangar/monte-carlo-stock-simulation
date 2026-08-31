"""
Monte Carlo Stock Price Simulation
 
Quick and dirty GBM-style simulation: pull historical prices, estimate
drift/volatility from them, then fire off a few thousand random walks
to see where the price might land.
 
Run with: python simulation.py
"""
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
 
# ---- change these if you want a different ticker/window/etc ----
TICKER = "AAPL"        # try "SPY" if you just want the broad market
START = "2022-01-01"   # how far back to pull history for the stats
DAYS = 30               # how many trading days to project forward
SIMS = 5000             # more sims = smoother histogram, slower run
PLOT_PATHS = 100        # only draw a subset of paths, otherwise the chart's a mess
 
# grab the price history
data = yf.download(TICKER, start=START, progress=False)
prices = data["Adj Close"].dropna()
returns = prices.pct_change().dropna()
 
# mean/std of daily returns -- these drive the whole simulation
mu = returns.mean()
sigma = returns.std()
last_price = float(prices.iloc[-1])
 
# sample DAYS worth of random daily returns for each of the SIMS simulations,
# assuming they're normally distributed (a simplification, but a common one)
rand_rets = np.random.normal(mu, sigma, size=(SIMS, DAYS))
 
# turn each row of daily returns into an actual price path
price_paths = last_price * np.cumprod(1 + rand_rets, axis=1)
 
terminal = price_paths[:, -1]  # where each path ends up
prob_up = (terminal > last_price).mean()
 
# fan chart -- just a bunch of semi-transparent lines so you can see the spread
plt.figure(figsize=(10, 6))
for i in range(min(PLOT_PATHS, SIMS)):
    plt.plot(np.concatenate([[last_price], price_paths[i]]), linewidth=0.7, alpha=0.5)
plt.title(f"{TICKER} Monte Carlo Simulation ({DAYS} trading days)")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("paths.png", dpi=150)
plt.close()
 
# histogram of where all the simulations ended up
plt.figure(figsize=(10, 6))
plt.hist(terminal, bins=50)
plt.axvline(last_price, linestyle="--")  # dashed line marks today's price
plt.title(f"Distribution of Terminal Prices after {DAYS} days")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("terminal_hist.png", dpi=150)
plt.close()
 
print(f"Start price: {last_price:.2f}")
print(f"Probability price is higher after {DAYS} days: {prob_up:.1%}")
print("Saved plots: paths.png, terminal_hist.png")

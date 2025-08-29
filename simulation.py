# Monte Carlo Stock Price Simulation
# Run: python simulation.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# --------- CONFIG ---------
TICKER = "AAPL"       # e.g., "SPY" for S&P 500 ETF
START = "2022-01-01"  # historical data start date
DAYS = 30             # forecast horizon
SIMS = 5000           # number of simulated paths
PLOT_PATHS = 100      # how many paths to draw for the fan chart
# --------------------------

# 1) Download data
data = yf.download(TICKER, start=START, progress=False)
prices = data["Adj Close"].dropna()
returns = prices.pct_change().dropna()

# 2) Estimate parameters
mu = returns.mean()
sigma = returns.std()
last_price = float(prices.iloc[-1])

# 3) Simulate paths
# Draw normal daily returns with mean mu and std sigma
rand_rets = np.random.normal(mu, sigma, size=(SIMS, DAYS))
# Convert to price paths (cumulative product)
price_paths = last_price * np.cumprod(1 + rand_rets, axis=1)

# Terminal distribution & simple stat
terminal = price_paths[:, -1]
prob_up = (terminal > last_price).mean()

# 4) Plot: fan chart of paths
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

# 5) Plot: histogram of terminal prices
plt.figure(figsize=(10, 6))
plt.hist(terminal, bins=50)
plt.axvline(last_price, linestyle="--")
plt.title(f"Distribution of Terminal Prices after {DAYS} days")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("terminal_hist.png", dpi=150)
plt.close()

print(f"Start price: {last_price:.2f}")
print(f"Probability price is higher after {DAYS} days: {prob_up:.1%}")
print("Saved plots: paths.png, terminal_hist.png")

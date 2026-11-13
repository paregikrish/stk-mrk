# Stock Market (stk-mrk)

I'm a 20-year-old BCom graduate from India, and I'm learning Python to move into AI/ML and fintech. This repo is my learning journey, built in public, one working piece at a time. It is not a polished product. It is a beginner's honest progress log that turns into a real tool.

## The big goal

Imagine a client with Rs 10 lakh asks: **"Which of these companies gave the best return for the risk taken, and do they move together?"**

I want to build a tool that answers that with real market data. Right now it can pull and show the data. Next it learns to analyse it.

## What it does today (Day 1)

`pull1.py` is a small menu program:

1. Asks for a region: `India` or `US`
2. Asks for a time period: 1, 5, 10, 15 or 20 days
3. Downloads the prices of 10 big companies from that region using `yfinance`
4. Prints four tables: Close, High, Low and Volume
5. Asks "Explore another?" and repeats until the user type `no`

Bad input (like region `UK`) gives a friendly message instead of a crash.

## How to run it

```bash
python3 -m venv venv
source venv/bin/activate
pip install yfinance
python pull1.py
```

## My Day 1 journey

I started knowing only variables, data types, `input()` and `if/else`. In one day I learnt:

- **Git basics:** `git init`, `.gitignore`, staging and committing
- **Virtual environments:** keeping project libraries separate
- **yfinance and pandas:** downloading market data into a DataFrame, and why many stocks produce a MultiIndex (two levels of column names)
- **Dictionaries:** mapping what the user types to what the code needs, including nested dictionaries and `.get()`
- **f-strings:** putting values inside printed text
- **`while` loops:** making the tool repeat until the user quits
- **Debugging:** reading a traceback from the bottom up. My best bug was passing a whole dictionary where yfinance wanted a text like `"10d"`.

## Known issues (I'm not hiding them)

- The first run is written twice in the file, once outside the loop and once inside it. I plan to merge them so the loop does every run.
- The newest day's row can be partial while a market is still open, so its Close, High, Low and Volume are not final.
- Indian prices are in rupees and US prices in dollars, so they must never be compared directly.

## Roadmap

- [ ] Clean the file so the loop does the first run too
- [ ] Clean the data and check for missing values and odd jumps
- [ ] Daily returns, volatility, max drawdown
- [ ] Sharpe ratio (return for the risk taken)
- [ ] Correlation between stocks (do they move together?)
- [ ] Store data in SQLite and query it with SQL
- [ ] Charts with matplotlib
- [ ] Let the user type **any** company ticker and analyse it, using a market-data API
- [ ] One final script that runs the whole pipeline

## Tech used

Python, yfinance, Git

---
*Built by Krish, learning in public.*

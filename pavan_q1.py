import pandas as pd
import numpy as np


df = pd.read_csv('NQ_OHLC.csv')
df['Date-Time'] = pd.to_datetime(df['Date-Time'])
df.set_index('Date-Time', inplace=True)


df = df[df['Close'] > 0]

numerator = df['Close'] - df['Low']
denominator = df['High'] - df['Low']


df['raw_alpha'] = (numerator / denominator.replace(0, np.nan)).fillna(0.5)

df['smoothed_alpha'] = df['raw_alpha'].rolling(window=3).mean()


df['Signal'] = -1 * np.sign(df['smoothed_alpha'] - 0.4)


df['Position'] = df['Signal'].fillna(0)


df['Asset_Ret'] = np.log(df['Close'] / df['Close'].shift(1))


df['Strategy_Ret'] = df['Position'].shift(1) * df['Asset_Ret']


clean_returns = df['Strategy_Ret'].dropna()


seconds_per_year = 252 * 6.5 * 3600
annualization_factor = np.sqrt(seconds_per_year)

if clean_returns.std() != 0:
    sharpe_ratio = (clean_returns.mean() / clean_returns.std()) * annualization_factor
    total_return = np.exp(clean_returns.cumsum().iloc[-1]) - 1
else:
    sharpe_ratio = 0.0
    total_return = 0.0


print(f"--- Alpha Performance Report ---")
print(f"Strategy Sharpe Ratio: {sharpe_ratio:.4f}")
print(f"Total Cumulative Return: {total_return:.2%}")
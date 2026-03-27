# Alpha_PV_1
An alpha based on Price-Volume data, achieving a Sharpe Ratio of 16.7.

## Overview
This alpha is based on the ratio between the range of the close (Close - Low) relative to the total period range (High - Low). I have used **Python** to implement this strategy using standard data science libraries (Pandas/NumPy).

## Hypothesis
The Alpha is built on the **Mean Reversion** concept:
Close near High → Price is locally overextended/overbought → Action: SHORT
Close near Low → Price is locally oversold → Action: LONG

By smoothing these signals over a short window, the alpha captures short-term price exhaustion points.

## How to Use
1. **Data:** Download the _NQ_OHLC.csv_ dataset provided in the repository.
2. **Setup:** Place the dataset and the alpha Python file in the same directory on your PC.
3. **Run:** Execute the script. You should see the following performance report:


--- Alpha Performance Report ---
Strategy Sharpe Ratio: 16.7566
Total Cumulative Return: 9.25%

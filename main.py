import pandas as pd
import numpy as np
import yfinance as yf

rets = yf.download('NVDA', start='2020-01-01', end='2025-01-01', auto_adjust=True)


print(rets.tail())
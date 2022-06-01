import yfinance as yf
import pandas as pd
from sklearn import DecisionTreeClassifier

ticker = yf.Ticker(input("Enter a ticker: "))
ticker_data = ticker.history(period="max")

model = DecisionTreeClassifier()

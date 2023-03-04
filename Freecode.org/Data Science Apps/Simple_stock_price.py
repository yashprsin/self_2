import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple stock price

Shown are the stock **closing price** and ***volume*** of Google !

""")


tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')

st.write("""## Closing price""")
st.line_chart(tickerDf.Close)
st.write("""## Volume""")
st.line_chart(tickerDf.Volume)
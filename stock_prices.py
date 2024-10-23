import matplotlib.pyplot as plt
import yfinance as yf
import webbrowser

#href="https://medium.com/@kasperjuunge/yfinance-10-ways-to-get-stock-data-with-python-6677f49e8282"
#get stock data

data = yf.download(["MSFT","AAPL"], start="2020-01-01", end="2021-01-01")


data['Close'].plot()
plt.title("Microsoft and Apple Stock Prices")
plt.show()
import yfinance as yf

def fetch_market_data(tickers):
    data = {}
    for ticker in tickers:
        ticker_obj = yf.Ticker(ticker)
        hist = ticker_obj.history(period="1d")
        if not hist.empty:
            latest = hist.iloc[-1]
            data[ticker] = {
                "price": round(latest["Close"], 2),
                "change": round(latest["Close"] - latest["Open", 2], 2),
                "percent_change": round(((latest["Close"] - latest["Open"]) / latest["Open"]) * 100, 2) 
            }
    return data

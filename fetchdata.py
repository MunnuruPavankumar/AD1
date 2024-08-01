import ccxt
import pandas as pd


# Initialize the Binance exchange
exchange = ccxt.binance()

# Define the symbol and timeframe
symbol = 'BTC/USDT'
timeframe = '1h'

# Fetch historical OHLCV data
ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

# Convert the data to a DataFrame
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime

# Save the data to a CSV file
df.to_csv('historical_data.csv', index=False)
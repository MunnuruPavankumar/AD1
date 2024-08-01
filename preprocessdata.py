import pandas as pd
import ta
from ta import add_all_ta_features

# Load historical data
df = pd.read_csv('historical_data.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Resample to hourly timeframe
df_hourly = df.resample('H').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
})

# Calculate hourly returns
df_hourly['returns'] = df_hourly['close'].pct_change()

# Calculate hourly moving averages
df_hourly['ma10'] = df_hourly['close'].rolling(window=10).mean()
df_hourly['ma50'] = df_hourly['close'].rolling(window=50).mean()

# Calculate Relative Strength Index (RSI)
df_hourly['rsi'] = ta.momentum.RSIIndicator(df_hourly['close']).rsi()

# Calculate historical volatility
df_hourly['volatility'] = df_hourly['returns'].rolling(window=20).std()

# Add lagged returns
df_hourly['lag1'] = df_hourly['returns'].shift(1)
df_hourly['lag2'] = df_hourly['returns'].shift(2)

# Drop rows with missing values
df_hourly.dropna(inplace=True)

# Print the preprocessed data
print(df_hourly.tail())
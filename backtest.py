#implement trading strategy
from trainandevaluate import model, X_test
from preprocessdata import df_hourly
# Predict returns using the trained model
predicted_returns = model.predict(X_test)

# Create trading signals based on predicted returns
threshold = 0.001  # Set your own threshold
trading_signals = [1 if ret > threshold else -1 if ret < -threshold else 0 for ret in predicted_returns]

# Print the trading signals
print("Trading Signals:", trading_signals)

#backtest strategy
import matplotlib.pyplot as plt

# Assuming you have historical returns data (replace this with your actual data)
historical_returns = df_hourly['returns'].loc[X_test.index]

# Trim the last element from historical_returns
historical_returns = historical_returns[:-1]

# Calculate strategy returns by multiplying trading signals with actual returns
strategy_returns = trading_signals[:-1] * historical_returns.values

# Calculate cumulative returns
cumulative_returns = (1 + strategy_returns).cumprod()

# Plot the cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(cumulative_returns, label='Strategy Cumulative Returns', color='blue')
plt.title('Backtest of Trading Strategy')
plt.xlabel('Time')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.show()
#SPLITTING DATA
import sklearn
from sklearn.model_selection import train_test_split
from preprocessdata import df_hourly

# Define features (X) and target (y)
features = ['open', 'high', 'low', 'close', 'volume', 'returns', 'ma10', 'ma50', 'rsi', 'volatility', 'lag1', 'lag2']
target = 'returns'

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(df_hourly[features], df_hourly[target], test_size=0.2, random_state=42)

# Print the shapes of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)
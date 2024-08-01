#TRAIN EVALUATE MODEL
from splitingdata import X_test, X_train, y_test, y_train
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Define features (X) and target (y)
features = ['open', 'high', 'low', 'close', 'volume', 'returns', 'ma10', 'ma50', 'rsi', 'volatility', 'lag1', 'lag2']
target = 'returns'

# Best hyperparameters obtained from the tuning step
best_params = {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}

# Initialize the Random Forest Regressor with the best hyperparameters
model = RandomForestRegressor(**best_params)

# Train the model
model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
print("R-squared score on the testing set:", r2)
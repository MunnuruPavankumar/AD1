#TUNNING MODEL
from splitingdata import X_train, y_train
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor  # You can replace this with any other regression model

# Define features (X) and target (y)
features = ['open', 'high', 'low', 'close', 'volume', 'returns', 'ma10', 'ma50', 'rsi', 'volatility', 'lag1', 'lag2']
target = 'returns'

# Define the number of folds for cross-validation
n_folds = 5

# Initialize the Random Forest Regressor
model = RandomForestRegressor()

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize GridSearchCV
grid_search = GridSearchCV(model, param_grid, cv=n_folds, scoring='r2', n_jobs=-1)

# Fit the model to the data
grid_search.fit(X_train, y_train)

# Print the best hyperparameters
print("Best Hyperparameters:", grid_search.best_params_)
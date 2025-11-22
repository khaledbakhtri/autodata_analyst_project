from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
import numpy as np

class MLTrainingEngine:
    """Trains AI models to predict market movements"""
    
    def train_ensemble_model(self, X, y):
        """Uses multiple models for better predictions"""
        
        models = {
            'random_forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'gradient_boost': GradientBoostingClassifier(n_estimators=100, random_state=42)
        }
        
        # Special validation for time series data
        tscv = TimeSeriesSplit(n_splits=3)
        results = {}
        
        for name, model in models.items():
            predictions, actuals = [], []
            
            for train_idx, test_idx in tscv.split(X):
                X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
                y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
                
                # Clean the data
                X_train = X_train.fillna(0)
                X_test = X_test.fillna(0)
                
                # Standardize features
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                
                # Train and test the model
                model.fit(X_train_scaled, y_train)
                preds = model.predict(X_test_scaled)
                
                predictions.extend(preds)
                actuals.extend(y_test)
            
            if len(predictions) > 0:
                accuracy = np.mean(np.array(predictions) == np.array(actuals))
                results[name] = {
                    'accuracy': round(accuracy, 3),
                    'samples': len(predictions)
                }
        
        return results

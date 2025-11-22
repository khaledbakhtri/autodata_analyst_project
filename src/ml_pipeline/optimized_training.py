
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
import numpy as np

class OptimizedMLTrainingEngine:
    """Optimized model training with feature selection"""
    
    def train_optimized_models(self, X, y):
        """Trains models with feature selection and hyperparameter tuning"""
        
        # Handle constant features before selection
        X_clean = X.loc[:, X.nunique() > 1]  # Remove constant features
        
        # Feature selection - FIXED VERSION
        if X_clean.shape[1] > 1:
            selector = SelectKBest(f_classif, k=min(15, X_clean.shape[1]))
            X_selected = selector.fit_transform(X_clean, y)
            selected_features = X_clean.columns[selector.get_support()]
        else:
            X_selected = X_clean.values
            selected_features = X_clean.columns
        
        models = {
            'random_forest': RandomForestClassifier(
                n_estimators=200, 
                max_depth=10, 
                min_samples_split=10,
                random_state=42
            ),
            'gradient_boost': GradientBoostingClassifier(
                n_estimators=200,
                max_depth=6,
                learning_rate=0.1,
                random_state=42
            )
        }
        
        tscv = TimeSeriesSplit(n_splits=3)
        results = {}
        
        for name, model in models.items():
            predictions, actuals = [], []
            
            for train_idx, test_idx in tscv.split(X_selected):
                X_train, X_test = X_selected[train_idx], X_selected[test_idx]
                y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
                
                # Handle any remaining NaNs
                X_train = np.nan_to_num(X_train)
                X_test = np.nan_to_num(X_test)
                
                # Standardize features
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                
                # Train and test
                model.fit(X_train_scaled, y_train)
                preds = model.predict(X_test_scaled)
                
                predictions.extend(preds)
                actuals.extend(y_test)
            
            if len(predictions) > 0:
                accuracy = np.mean(np.array(predictions) == np.array(actuals))
                results[name] = {
                    'accuracy': round(accuracy, 3),
                    'samples': len(predictions),
                    'selected_features': list(selected_features)
                }
        
        return results

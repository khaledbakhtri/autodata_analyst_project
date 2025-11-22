import pandas as pd
import numpy as np

class FeatureEngine:
    """Builds smart features from raw market data"""
    
    def create_advanced_features(self, df: pd.DataFrame):
        """Transforms raw prices into predictive features"""
        df = df.copy()
        
        # Price movements
        df['daily_returns'] = df['Close'].pct_change()
        
        # Trend indicators
        for days in [5, 10, 20]:
            df[f'sma_{days}'] = df['Close'].rolling(days).mean()
            df[f'trend_{days}'] = df['Close'] / df[f'sma_{days}'] - 1
        
        # Market volatility
        df['volatility_10d'] = df['daily_returns'].rolling(10).std()
        
        # Trading activity
        df['volume_sma_20'] = df['Volume'].rolling(20).mean()
        df['volume_boost'] = df['Volume'] / df['volume_sma_20']
        
        # What we're trying to predict: will stock go up in next 5 days?
        df['target'] = (df['Close'].shift(-5) > df['Close']).astype(int)
        
        return df.dropna()

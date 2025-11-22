
import pandas as pd
import numpy as np
from typing import List

class EnhancedFeatureEngine:
    """Advanced feature engineering for better predictions"""
    
    def create_enhanced_features(self, df: pd.DataFrame, symbol: str = ""):
        """Creates more sophisticated trading features"""
        df = df.copy()
        
        # 1. Price-based features
        df['returns'] = df['Close'].pct_change()
        df['log_returns'] = np.log(df['Close'] / df['Close'].shift(1))
        
        # 2. Multiple moving averages
        for window in [5, 10, 20, 50]:
            df[f'sma_{window}'] = df['Close'].rolling(window).mean()
            df[f'ema_{window}'] = df['Close'].ewm(span=window).mean()
            df[f'price_vs_sma_{window}'] = df['Close'] / df[f'sma_{window}'] - 1
        
        # 3. Volatility features
        df['volatility_5d'] = df['returns'].rolling(5).std()
        df['volatility_20d'] = df['returns'].rolling(20).std()
        df['volatility_ratio'] = df['volatility_5d'] / df['volatility_20d']
        
        # 4. Volume features
        df['volume_sma_10'] = df['Volume'].rolling(10).mean()
        df['volume_ratio'] = df['Volume'] / df['volume_sma_10']
        df['volume_price_trend'] = df['Volume'] * df['returns']
        
        # 5. Price momentum
        df['momentum_5'] = df['Close'] / df['Close'].shift(5) - 1
        df['momentum_10'] = df['Close'] / df['Close'].shift(10) - 1
        df['rsi_14'] = self.calculate_rsi(df['Close'], 14)
        
        # 6. Support and resistance levels
        df['resistance_20'] = df['High'].rolling(20).max()
        df['support_20'] = df['Low'].rolling(20).min()
        df['price_vs_resistance'] = df['Close'] / df['resistance_20'] - 1
        df['price_vs_support'] = df['Close'] / df['support_20'] - 1
        
        # 7. Market regime detection - FIXED VERSION
        df['trend_strength'] = df['Close'].rolling(20).apply(
            lambda x: (x.iloc[-1] - x.iloc[0]) / (x.std() + 1e-8)
        )
        
        # 8. Better target: Will price increase by 2% in next 5 days?
        df['target'] = (df['Close'].shift(-5) > df['Close'] * 1.02).astype(int)
        
        return df.dropna()
    
    def calculate_rsi(self, prices: pd.Series, window: int = 14):
        """Calculate Relative Strength Index"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

import yfinance as yf
import pandas as pd
from typing import Dict, List

class DataIngestionEngine:
    """Handles all data collection from financial markets"""
    
    def get_financial_data(self, symbols: List[str], period: str = "2y") -> Dict[str, pd.DataFrame]:
        """Gets stock data for multiple companies"""
        financial_data = {}
        
        for symbol in symbols:
            try:
                print(f"📊 Fetching {symbol}...")
                stock = yf.Ticker(symbol)
                hist = stock.history(period=period)
                
                if len(hist) > 100:
                    financial_data[symbol] = hist
                    print(f"✅ {symbol}: Got {len(hist)} days of data")
                else:
                    print(f"⚠️ {symbol}: Not enough data")
                    
            except Exception as e:
                print(f"❌ Failed on {symbol}: {e}")
        
        return financial_data

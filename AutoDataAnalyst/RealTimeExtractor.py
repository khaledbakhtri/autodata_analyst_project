
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime  # Correct import
import logging

class RealTimeExtractor:
    """Fixed RealTimeExtractor with correct datetime imports"""
    
    def __init__(self):
        self.logger = logging.getLogger('AutoDataAnalyst.RealTimeExtractor')
        
    def get_financial_data(self, symbols=None):
        """Extract real-time financial data"""
        if symbols is None:
            symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
            
        current_time = datetime.now()  # This will work now
        self.logger.info(f"📊 Extracting financial data for {symbols} at {current_time}")
        data = {}
        
        for symbol in symbols:
            try:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                
                data[symbol] = {
                    'current_price': info.get('currentPrice', info.get('regularMarketPrice', 0)),
                    'market_cap': info.get('marketCap', 0),
                    'pe_ratio': info.get('trailingPE', 0),
                    'volume': info.get('volume', 0),
                    'company_name': info.get('longName', symbol)
                }
                self.logger.info(f"✅ Successfully fetched {symbol}")
                
            except Exception as e:
                self.logger.error(f"❌ Error fetching {symbol}: {e}")
                data[symbol] = None
                
        return data

    def get_historical_data(self, symbol, period="1y"):
        """Get historical price data"""
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period)
            return hist
        except Exception as e:
            self.logger.error(f"Error getting historical data for {symbol}: {e}")
            return None

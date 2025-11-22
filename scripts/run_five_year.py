#!/usr/bin/env python3
"""
AutoDataAnalyst - 5-Year Data Pipeline
Processes historical financial data
"""

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    print("📊 AutoDataAnalyst - 5-Year Data Processing")
    print("=" * 50)
    
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    results = {}
    
    for symbol in symbols:
        try:
            logger.info(f"Processing {symbol}")
            ticker = yf.Ticker(symbol)
            
            # Get 5 years of data
            end_date = datetime.now()
            start_date = end_date - timedelta(days=5*365)
            
            hist_data = ticker.history(start=start_date, end=end_date)
            results[symbol] = {
                'data_points': len(hist_data),
                'period': f"{start_date.date()} to {end_date.date()}",
                'status': 'success'
            }
            print(f"✅ {symbol}: {len(hist_data)} trading days")
            
        except Exception as e:
            logger.error(f"Error processing {symbol}: {e}")
            results[symbol] = {'status': 'failed', 'error': str(e)}
            print(f"❌ {symbol}: Failed")
    
    print(f"\n📈 Processed {len([r for r in results.values() if r['status'] == 'success'])}/{len(symbols)} symbols")
    return results

if __name__ == "__main__":
    main()

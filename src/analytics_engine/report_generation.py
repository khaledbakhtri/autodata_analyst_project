
import pandas as pd
from datetime import datetime

class ReportGenerator:
    """Generate professional reports"""
    
    def __init__(self):
        """Initialize Report Generator"""
        pass
    
    def generate_trading_report(self, signals: dict, positions: dict, portfolio_value: float):
        """Generate a comprehensive trading report"""
        
        report = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'portfolio_value': portfolio_value,
            'signals': signals,
            'positions': positions,
            'total_allocated': sum(positions.values()),
            'cash_remaining': portfolio_value - sum(positions.values()),
            'allocation_rate': sum(positions.values()) / portfolio_value
        }
        
        return report
    
    def generate_execution_report(self, trades: list):
        """Generate trade execution report"""
        if not trades:
            return {"message": "No trades executed"}
            
        report = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_trades': len(trades),
            'buy_trades': len([t for t in trades if t.get('action') == 'BUY']),
            'sell_trades': len([t for t in trades if t.get('action') == 'SELL']),
            'trades': trades
        }
        
        return report

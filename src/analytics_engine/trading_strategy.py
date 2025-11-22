
import pandas as pd
from typing import Dict, List

class TradingStrategy:
    """Implements trading strategies based on model predictions"""
    
    def generate_signals(self, model_results: Dict, min_confidence: float = 0.55):
        """Generate trading signals based on model confidence"""
        
        signals = {}
        
        for symbol, results in model_results.items():
            if results:
                best_acc = max(r['accuracy'] for r in results.values())
                
                if best_acc >= min_confidence:
                    # Strong buy signal
                    if best_acc > 0.60:
                        signal = "STRONG_BUY"
                        confidence = "HIGH"
                    elif best_acc > 0.55:
                        signal = "BUY" 
                        confidence = "MEDIUM"
                    else:
                        signal = "HOLD"
                        confidence = "LOW"
                else:
                    signal = "HOLD"
                    confidence = "LOW"
                    
                signals[symbol] = {
                    'signal': signal,
                    'confidence': confidence,
                    'accuracy': best_acc,
                    'action': 'BUY' if signal in ['STRONG_BUY', 'BUY'] else 'HOLD'
                }
        
        return signals
    
    def calculate_position_size(self, signals: Dict, portfolio_value: float = 10000):
        """Calculate position sizes based on signal strength"""
        
        positions = {}
        strong_signals = [s for s in signals.values() if s['signal'] == 'STRONG_BUY']
        medium_signals = [s for s in signals.values() if s['signal'] == 'BUY']
        
        if strong_signals:
            # Allocate more to strong signals
            strong_allocation = portfolio_value * 0.6 / len(strong_signals)
            medium_allocation = portfolio_value * 0.4 / len(medium_signals) if medium_signals else 0
        else:
            strong_allocation = 0
            medium_allocation = portfolio_value * 1.0 / len(medium_signals) if medium_signals else 0
        
        for symbol, signal_info in signals.items():
            if signal_info['signal'] == 'STRONG_BUY':
                positions[symbol] = strong_allocation
            elif signal_info['signal'] == 'BUY':
                positions[symbol] = medium_allocation
            else:
                positions[symbol] = 0
                
        return positions

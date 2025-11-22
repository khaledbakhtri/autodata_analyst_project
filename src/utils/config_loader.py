
import yaml
import os
from typing import Dict, Any

class ConfigLoader:
    """Configuration loader for the trading pipeline"""
    
    def __init__(self, config_path: str = "config/config.yaml"):
        """Initialize config loader with path to config file"""
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as file:
                    return yaml.safe_load(file) or {}
            else:
                print(f"⚠️ Config file not found at {self.config_path}, using defaults")
                return self._get_default_config()
        except Exception as e:
            print(f"❌ Error loading config: {e}, using defaults")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            'data_sources': {
                'yahoo_finance': True,
                'period': '1y',
                'symbols': ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN']
            },
            'model_training': {
                'validation_splits': 3,
                'min_samples': 20,
                'min_confidence': 0.55
            },
            'trading': {
                'portfolio_value': 10000,
                'max_positions': 5,
                'risk_per_trade': 0.02
            }
        }
    
    def get(self, key: str, default=None):
        """Get configuration value by key"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def update_config(self, updates: Dict[str, Any]):
        """Update configuration with new values"""
        self.config.update(updates)
        self._save_config()
    
    def _save_config(self):
        """Save configuration to file"""
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            with open(self.config_path, 'w') as file:
                yaml.dump(self.config, file, default_flow_style=False)
        except Exception as e:
            print(f"❌ Error saving config: {e}")

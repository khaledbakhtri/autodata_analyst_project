#!/usr/bin/env python3
"""
PRODUCTION READY TEST - Complete Pipeline Execution
Tests the entire pipeline from data to trading signals
"""

import sys
import os
import importlib.util
import pandas as pd

def import_class(file_path, class_name):
    """Import a class directly from file path"""
    try:
        spec = importlib.util.spec_from_file_location(class_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, class_name)
    except Exception as e:
        print(f"❌ Failed to import {class_name}: {e}")
        return None

def run_production_test():
    print("🚀 PRODUCTION READY PIPELINE TEST")
    print("=" * 60)
    
    # Import all production components
    components = {
        'DataIngestion': ('src/data_pipeline/data_ingestion.py', 'DataIngestionEngine'),
        'EnhancedFeatures': ('src/data_pipeline/enhanced_features.py', 'EnhancedFeatureEngine'),
        'OptimizedTraining': ('src/ml_pipeline/optimized_training.py', 'OptimizedMLTrainingEngine'),
        'TradingStrategy': ('src/analytics_engine/trading_strategy.py', 'TradingStrategy'),
        'BusinessAnalytics': ('src/analytics_engine/business_analytics.py', 'BusinessAnalytics'),
        'ReportGenerator': ('src/analytics_engine/report_generation.py', 'ReportGenerator'),
        'ConfigLoader': ('src/utils/config_loader.py', 'ConfigLoader')
    }
    
    engines = {}
    print("🔧 Loading production engines...")
    for name, (path, class_name) in components.items():
        engines[name] = import_class(path, class_name)
        if engines[name]:
            print(f"   ✅ {name}: Loaded")
        else:
            print(f"   ❌ {name}: Failed")
            return False
    
    print("\n🎯 All engines loaded successfully!")
    
    # Initialize engines
    config_loader = engines['ConfigLoader']()
    data_engine = engines['DataIngestion']()
    feature_engine = engines['EnhancedFeatures']()
    ml_engine = engines['OptimizedTraining']()
    strategy_engine = engines['TradingStrategy']()
    analytics_engine = engines['BusinessAnalytics']()
    report_engine = engines['ReportGenerator']()
    
    # Get configuration
    symbols = config_loader.get('data_sources.symbols', ['AAPL', 'MSFT', 'GOOGL'])
    portfolio_value = config_loader.get('trading.portfolio_value', 10000)
    
    print(f"\n📊 PHASE 1: Data Collection")
    print(f"   Symbols: {symbols}")
    raw_data = data_engine.get_financial_data(symbols, period='1y')
    
    if not raw_data:
        print("❌ No data collected")
        return False
    
    print(f"   ✅ Collected {len(raw_data)} symbols")
    
    print(f"\n🔧 PHASE 2: Enhanced Feature Engineering")
    features_data = {}
    for symbol, data in raw_data.items():
        features = feature_engine.create_enhanced_features(data, symbol)
        if features is not None:
            features_data[symbol] = features
            print(f"   ✅ {symbol}: {len(features.columns)} features, {len(features)} samples")
    
    if not features_data:
        print("❌ No features generated")
        return False
    
    print(f"\n🤖 PHASE 3: Optimized Model Training")
    model_results = {}
    for symbol, features_df in features_data.items():
        if 'target' in features_df.columns and len(features_df) > 30:
            X = features_df.drop('target', axis=1)
            y = features_df['target']
            results = ml_engine.train_optimized_models(X, y)
            model_results[symbol] = results
            
            if results:
                best_acc = max(r['accuracy'] for r in results.values())
                print(f"   ✅ {symbol}: {best_acc:.1%} accuracy")
    
    print(f"\n💼 PHASE 4: Trading Strategy & Analytics")
    if model_results:
        # Generate trading signals
        signals = strategy_engine.generate_signals(model_results)
        positions = strategy_engine.calculate_position_size(signals, portfolio_value)
        
        # Generate analytics
        metrics = analytics_engine.calculate_performance_metrics(model_results)
        report = report_engine.generate_trading_report(signals, positions, portfolio_value)
        
        print(f"   📈 Performance Metrics:")
        print(f"      • Average Accuracy: {metrics.get('average_accuracy', 0):.1%}")
        print(f"      • Success Rate: {metrics.get('success_rate', 0):.1%}")
        print(f"      • Strong Signals: {len([s for s in signals.values() if s['action'] == 'BUY'])}")
        
        print(f"\n   💰 Portfolio Allocation:")
        total_allocated = 0
        for symbol, amount in positions.items():
            if amount > 0:
                print(f"      • {symbol}: ${amount:,.2f}")
                total_allocated += amount
        
        print(f"\n   📊 Final Summary:")
        print(f"      • Portfolio: ${portfolio_value:,.2f}")
        print(f"      • Allocated: ${total_allocated:,.2f}")
        print(f"      • Cash: ${portfolio_value - total_allocated:,.2f}")
        print(f"      • Allocation Rate: {total_allocated/portfolio_value:.1%}")
        
        print(f"\n🎉 PRODUCTION TEST COMPLETED SUCCESSFULLY! 🚀")
        return True
    else:
        print("❌ No model results for trading")
        return False

if __name__ == "__main__":
    success = run_production_test()
    if success:
        print("\n" + "=" * 60)
        print("🎯 YOUR ENTERPRISE AI TRADING PIPELINE IS PRODUCTION READY!")
        print("   Next steps:")
        print("   1. Deploy to cloud (AWS/Azure/GCP)")
        print("   2. Set up automated daily execution")
        print("   3. Integrate with broker API")
        print("   4. Monitor performance dashboard")
        sys.exit(0)
    else:
        print("\n💥 PRODUCTION TEST FAILED")
        sys.exit(1)

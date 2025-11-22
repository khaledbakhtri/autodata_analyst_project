#!/usr/bin/env python3
"""
FINAL VERIFICATION - Enterprise AI Trading Pipeline
Verifies all components are working correctly
"""

import sys
import os
import importlib.util

def verify_component(file_path, class_name, component_name):
    """Verify a single component can be imported and instantiated"""
    try:
        spec = importlib.util.spec_from_file_location(class_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        engine_class = getattr(module, class_name)
        engine_instance = engine_class()
        return True, f"✅ {component_name}: OK"
    except Exception as e:
        return False, f"❌ {component_name}: {e}"

def main():
    print("🔍 FINAL PIPELINE VERIFICATION")
    print("=" * 50)
    
    components = [
        ('src/data_pipeline/data_ingestion.py', 'DataIngestionEngine', 'Data Ingestion'),
        ('src/data_pipeline/feature_engineering.py', 'FeatureEngine', 'Feature Engineering'),
        ('src/data_pipeline/enhanced_features.py', 'EnhancedFeatureEngine', 'Enhanced Features'),
        ('src/ml_pipeline/model_training.py', 'MLTrainingEngine', 'ML Training'),
        ('src/ml_pipeline/optimized_training.py', 'OptimizedMLTrainingEngine', 'Optimized Training'),
        ('src/analytics_engine/trading_strategy.py', 'TradingStrategy', 'Trading Strategy'),
        ('src/analytics_engine/business_analytics.py', 'BusinessAnalytics', 'Business Analytics'),
        ('src/analytics_engine/report_generation.py', 'ReportGenerator', 'Report Generation'),
        ('src/utils/config_loader.py', 'ConfigLoader', 'Config Loader')
    ]
    
    all_ok = True
    for file_path, class_name, component_name in components:
        if os.path.exists(file_path):
            success, message = verify_component(file_path, class_name, component_name)
            print(message)
            if not success:
                all_ok = False
        else:
            print(f"❌ {component_name}: File not found")
            all_ok = False
    
    print("\n" + "=" * 50)
    if all_ok:
        print("🎉 ALL COMPONENTS VERIFIED! Pipeline is ready!")
        return True
    else:
        print("💥 SOME COMPONENTS FAILED VERIFICATION")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

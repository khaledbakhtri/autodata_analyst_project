# API Documentation - Auto-Generated

> **Automatically generated from source code** | **Last Updated: 2024**

## Overview

This documentation is automatically generated from the source code of the Enterprise AI Analytics Pipeline.

## Core Modules


### 📁 __init__

No classes found in this module.

### 📁 utils.config_loader

#### 🏗 ConfigLoader

**Description**: Configuration loader for the trading pipeline

**Methods**:

- `__init__(self, config_path)`
  - Initialize config loader with path to config file

- `_load_config(self)`
  - Load configuration from YAML file

- `_get_default_config(self)`
  - Get default configuration

- `get(self, key, default)`
  - Get configuration value by key

- `update_config(self, updates)`
  - Update configuration with new values

- `_save_config(self)`
  - Save configuration to file


### 📁 utils.__init__

No classes found in this module.

### 📁 analytics_engine.report_generation

#### 🏗 ReportGenerator

**Description**: Generate professional reports

**Methods**:

- `__init__(self)`
  - Initialize Report Generator

- `generate_trading_report(self, signals, positions, portfolio_value)`
  - Generate a comprehensive trading report

- `generate_execution_report(self, trades)`
  - Generate trade execution report


### 📁 analytics_engine.__init__

No classes found in this module.

### 📁 analytics_engine.business_analytics

#### 🏗 BusinessAnalytics

**Description**: Business intelligence and performance analytics

**Methods**:

- `__init__(self)`
  - Initialize Business Analytics engine

- `calculate_performance_metrics(self, model_results)`
  - Calculate key performance metrics

- `generate_performance_report(self, model_results)`
  - Generate a comprehensive performance report

- `_generate_analysis(self, metrics)`
  - Generate analysis based on performance metrics


### 📁 analytics_engine.trading_strategy

#### 🏗 TradingStrategy

**Description**: Implements trading strategies based on model predictions

**Methods**:

- `generate_signals(self, model_results, min_confidence)`
  - Generate trading signals based on model confidence

- `calculate_position_size(self, signals, portfolio_value)`
  - Calculate position sizes based on signal strength


### 📁 data_pipeline.__init__

No classes found in this module.

### 📁 data_pipeline.feature_engineering

#### 🏗 FeatureEngine

**Description**: Builds smart features from raw market data

**Methods**:

- `create_advanced_features(self, df)`
  - Transforms raw prices into predictive features


### 📁 data_pipeline.enhanced_features

#### 🏗 EnhancedFeatureEngine

**Description**: Advanced feature engineering for better predictions

**Methods**:

- `create_enhanced_features(self, df, symbol)`
  - Creates more sophisticated trading features

- `calculate_rsi(self, prices, window)`
  - Calculate Relative Strength Index


### 📁 data_pipeline.data_ingestion

#### 🏗 DataIngestionEngine

**Description**: Handles all data collection from financial markets

**Methods**:

- `get_financial_data(self, symbols, period)`
  - Gets stock data for multiple companies


### 📁 ml_pipeline.ensemble_methods

No classes found in this module.

### 📁 ml_pipeline.__init__

No classes found in this module.

### 📁 ml_pipeline.model_training

#### 🏗 MLTrainingEngine

**Description**: Trains AI models to predict market movements

**Methods**:

- `train_ensemble_model(self, X, y)`
  - Uses multiple models for better predictions


### 📁 ml_pipeline.optimized_training

#### 🏗 OptimizedMLTrainingEngine

**Description**: Optimized model training with feature selection

**Methods**:

- `train_optimized_models(self, X, y)`
  - Trains models with feature selection and hyperparameter tuning


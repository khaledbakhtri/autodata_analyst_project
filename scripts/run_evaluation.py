#!/usr/bin/env python3
"""
AutoDataAnalyst - Model Evaluation Script
Evaluates model performance with comprehensive metrics
"""

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(y_true, y_pred, y_proba=None):
    """Comprehensive model evaluation"""
    print("🎯 MODEL PERFORMANCE EVALUATION")
    print("=" * 40)
    
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    print(f"📊 Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"🎯 Precision: {precision:.4f} ({precision*100:.2f}%)")
    print(f"🔍 Recall: {recall:.4f} ({recall*100:.2f}%)")
    print(f"⚖️ F1-Score: {f1:.4f} ({f1*100:.2f}%)")
    
    if y_proba is not None:
        roc_auc = roc_auc_score(y_true, y_proba)
        print(f"📈 ROC-AUC: {roc_auc:.4f} ({roc_auc*100:.2f}%)")
    
    print("\n📋 Classification Report:")
    print(classification_report(y_true, y_pred))
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'roc_auc': roc_auc if y_proba is not None else None
    }

def main():
    print("🚀 AutoDataAnalyst - Model Evaluation")
    print("=" * 40)
    
    # Simulate test data (replace with your actual model)
    np.random.seed(42)
    y_true = np.random.randint(0, 2, 1000)
    y_pred = y_true + np.random.randint(-1, 2, 1000)
    y_pred = np.clip(y_pred, 0, 1)
    y_proba = np.random.rand(1000)
    
    results = evaluate_model(y_true, y_pred, y_proba)
    
    print("✅ Evaluation complete!")
    return results

if __name__ == "__main__":
    main()


import pandas as pd
import numpy as np

class BusinessAnalytics:
    """Business intelligence and performance analytics"""
    
    def __init__(self):
        """Initialize Business Analytics engine"""
        pass
    
    def calculate_performance_metrics(self, model_results: dict):
        """Calculate key performance metrics"""
        metrics = {}
        
        if model_results:
            accuracies = []
            for symbol, results in model_results.items():
                if results:
                    best_acc = max(r['accuracy'] for r in results.values())
                    accuracies.append(best_acc)
            
            if accuracies:
                metrics['average_accuracy'] = np.mean(accuracies)
                metrics['max_accuracy'] = np.max(accuracies)
                metrics['min_accuracy'] = np.min(accuracies)
                metrics['success_rate'] = len([acc for acc in accuracies if acc > 0.55]) / len(accuracies)
                metrics['total_symbols'] = len(accuracies)
        
        return metrics
    
    def generate_performance_report(self, model_results: dict):
        """Generate a comprehensive performance report"""
        metrics = self.calculate_performance_metrics(model_results)
        
        report = {
            'performance_metrics': metrics,
            'timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
            'analysis': self._generate_analysis(metrics)
        }
        
        return report
    
    def _generate_analysis(self, metrics: dict):
        """Generate analysis based on performance metrics"""
        if not metrics:
            return "No data available for analysis"
        
        analysis = []
        if metrics.get('average_accuracy', 0) > 0.55:
            analysis.append("📈 System performing above baseline (55% accuracy)")
        else:
            analysis.append("📉 System needs improvement")
            
        if metrics.get('success_rate', 0) > 0.5:
            analysis.append("🎯 Good signal success rate")
        else:
            analysis.append("⚠️ Low signal success rate")
            
        return " | ".join(analysis)

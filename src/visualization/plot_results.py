import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class ResultsVisualizer:
    """Visualize optimization and sensitivity analysis results"""
    
    def __init__(self):
        self.fig_count = 0
    
    def plot_convergence_curve(self, logbook, output_file='convergence_curve.png'):
        """Plot GA convergence curve"""
        gen = [record['gen'] for record in logbook]
        min_fitness = [record['min'] for record in logbook]
        avg_fitness = [record['avg'] for record in logbook]
        
        plt.figure(figsize=(10, 6))
        plt.plot(gen, min_fitness, 'b-', label='Best Fitness', linewidth=2)
        plt.plot(gen, avg_fitness, 'r--', label='Average Fitness', linewidth=2)
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Fitness Value', fontsize=12)
        plt.title('Genetic Algorithm Convergence', fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Convergence curve saved to {output_file}")
        plt.close()
    
    def plot_parameter_comparison(self, original_params, optimized_params, output_file='param_comparison.png'):
        """Compare original vs optimized parameters"""
        params = list(original_params.keys())
        original_values = list(original_params.values())
        optimized_values = list(optimized_params.values())
        
        x = np.arange(len(params))
        width = 0.35
        
        plt.figure(figsize=(12, 6))
        plt.bar(x - width/2, original_values, width, label='Original', color='steelblue')
        plt.bar(x + width/2, optimized_values, width, label='Optimized', color='coral')
        plt.xlabel('Parameters', fontsize=12)
        plt.ylabel('Parameter Values', fontsize=12)
        plt.title('Original vs Optimized Parameters', fontsize=14, fontweight='bold')
        plt.xticks(x, params, rotation=45)
        plt.legend()
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Parameter comparison saved to {output_file}")
        plt.close()
    
    def plot_field_vs_simulation(self, field_data, simulation_data, metric='queue_length', output_file='validation.png'):
        """Plot field data vs simulation results"""
        plt.figure(figsize=(10, 6))
        
        time_points = np.arange(len(field_data))
        plt.plot(time_points, field_data, 'o-', label='Field Data', linewidth=2, markersize=6)
        plt.plot(time_points, simulation_data, 's--', label='Simulation', linewidth=2, markersize=6)
        
        plt.xlabel('Time Interval', fontsize=12)
        plt.ylabel(metric.replace('_', ' ').title(), fontsize=12)
        plt.title(f'Field Data vs Simulation: {metric}', fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Validation plot saved to {output_file}")
        plt.close()
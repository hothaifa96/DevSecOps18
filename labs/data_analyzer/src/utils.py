import json
import os

def save_report(stats, file_path):
    """Save analysis report to a text file."""
    with open(file_path, 'w') as f:
        f.write("DATA ANALYSIS REPORT\n")
        f.write("===================\n\n")
        
        f.write(f"Record Count: {stats['count']}\n\n")
        
        f.write("Columns:\n")
        for col in stats['columns']:
            f.write(f"- {col}\n")
        f.write("\n")
        
        f.write("Numeric Columns:\n")
        for col in stats['numeric_columns']:
            f.write(f"- {col}\n")
        f.write("\n")
        
        f.write("Statistical Summary:\n")
        for col, summary in stats['stats_summary'].items():
            f.write(f"Column: {col}\n")
            for stat, value in summary.items():
                if isinstance(value, float):
                    f.write(f"  {stat}: {value:.4f}\n")
                else:
                    f.write(f"  {stat}: {value}\n")
            f.write("\n")
        
        f.write("\nEnd of Report\n")
import os
import pandas as pd
import matplotlib.pyplot as plt
from utils import save_report

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def analyze_data(data, output_dir):
    """Perform data analysis and generate reports."""
    if data is None:
        return False
    
    # Generate statistics
    stats = {
        'count': len(data),
        'columns': list(data.columns),
        'numeric_columns': list(data.select_dtypes(include=['number']).columns),
        'stats_summary': data.describe().to_dict(),
    }
    
    # Generate some plots
    for col in data.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(10, 6))
        plt.hist(data[col], bins=20)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.savefig(f"{output_dir}/{col}_distribution.png")
        plt.close()
    
    # Save the report
    report_path = f"{output_dir}/analysis_report.txt"
    save_report(stats, report_path)
    
    print(f"Analysis complete. Report saved to {report_path}")
    return True

def main():
    # Get environment variables or use defaults
    data_dir = os.environ.get('DATA_DIR', '/data')
    output_dir = os.environ.get('OUTPUT_DIR', '/output')
    file_name = os.environ.get('FILE_NAME', 'sample.csv')
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Load and analyze data
    file_path = os.path.join(data_dir, file_name)
    print(f"Loading data from {file_path}...")
    data = load_data(file_path)
    
    if data is not None:
        print(f"Data loaded successfully. Shape: {data.shape}")
        analyze_data(data, output_dir)
    else:
        print("Failed to load data. Exiting.")

if __name__ == "__main__":
    main()
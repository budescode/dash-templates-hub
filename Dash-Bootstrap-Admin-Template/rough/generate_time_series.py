import pandas as pd
import numpy as np
from datetime import date, timedelta
import os # Import os to handle file paths

def generate_revenue_data(days=30, save_csv=True):
    """Generates a mock DataFrame for Revenue and Profit over time and saves it."""
    
    # 1. Create a date range
    today = date.today()
    dates = [today - timedelta(days=i) for i in reversed(range(days))]
    
    # 2. Generate random walk data for Revenue and Profit (same as before)
    revenue_start = 10000
    profit_start = 4000
    
    rev_changes = np.random.normal(loc=100, scale=200, size=days).cumsum()
    prof_changes = np.random.normal(loc=50, scale=100, size=days).cumsum()
    
    revenue = revenue_start + rev_changes
    profit = profit_start + prof_changes

    # 3. Combine into a DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Revenue': revenue.round(2),
        'Profit': profit.round(2)
    })
    
    # 4. Generate data for the Traffic Source Donut Chart
    traffic_df = pd.DataFrame({
        'Source': ['Organic Search', 'Direct', 'Social Media', 'Referral'],
        'Percentage': [42.3, 31.8, 16.4, 9.5],
        'Users': [124592, 93672, 48316, 27950]
    })
    
    # 5. SAVE TO CSV
    if save_csv:
        # Define the file path (e.g., in a 'data' folder)
        output_file = os.path.join(os.getcwd(), 'data', 'revenue_analytics.csv')
        
        # Ensure the 'data' directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        df.to_csv(output_file, index=False) # index=False prevents writing the DataFrame index
        print(f"Data successfully saved to: {output_file}")
    
    return df, traffic_df

if __name__ == '__main__':
    revenue_df, traffic_df = generate_revenue_data(save_csv=True)
    print(revenue_df.head())
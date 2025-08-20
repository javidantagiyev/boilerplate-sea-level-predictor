import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.subplots(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = line1.intercept + line1.slope * x_pred
    plt.plot(x_pred, y_pred, color='red', label='Best Fit Line 1')
    

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    line2 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = line2.intercept + line2.slope * x_pred2
    plt.plot(x_pred2, y_pred2, color='green', label='Best Fit Line 2')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)') 
    plt.title('Rise in Sea Level')
 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
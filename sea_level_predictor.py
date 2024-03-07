import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def plot_line_of_best_fit(x, y, ax):
    linregressResults = linregress(x, y)
    slope = linregressResults.slope
    intercept = linregressResults.intercept
    x_line = np.arange(x.iloc[0], 2051)
    y_line = intercept + x_line * slope
    ax.plot(x_line, y_line)

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize = (16,8))
    ax.scatter(x, y)

    # Create first line of best fit
    plot_line_of_best_fit(x, y, ax)

    # Create second line of best fit
    x_2 = x.loc[x >= 2000]
    y_2 = y.loc[x_2.index]
    plot_line_of_best_fit(x_2, y_2, ax)

    # Add labels and title
    ax.set_xticks(np.arange(1850, 2100, 25))
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

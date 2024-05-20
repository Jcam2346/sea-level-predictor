import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
        df = pd.read_csv('epa-sea-level.csv', sep=',', header=0, dtype={'Year': int, 'CSIRO Adjusted Sea Level': float})

    # Create scatter plot
        plt.figure(1)
        plt.scatter(x = df.Year, y = (df['CSIRO Adjusted Sea Level']), marker = 'o', c = 'blue')

    # Create first line of best fit
        x_values = np.arange(df['Year'].min(), 2051, 1)
        sloper, intercept, r, p, std_err = linregress(x = df.Year, y = (df['CSIRO Adjusted Sea Level']))
        y_values = sloper * x_values + intercept
        plt.plot(x_values,(sloper * x_values + intercept), linestyle = '--', c = 'black')

    # Create second line of best fit
        df_2000 = df.loc[df.Year >= 2000]
        slope2, intercept2, r2, p2, std_err2 = linregress(x = df_2000.Year, y = (df_2000['CSIRO Adjusted Sea Level']))
        x_values_2000 = np.arange(2000, 2051, 1)
        plt.plot(x_values_2000,(x_values_2000*slope2+intercept2), linestyle = ':', c='red')

    # Add labels and title
        plt.xlabel('Year')
        plt.ylabel('Sea Level (inches)')
        plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
        plt.savefig('sea_level_plot.png')
        return plt.gca()

# draw_plot()
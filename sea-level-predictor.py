import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x= df['Year']
    y= df['CSIRO Adjusted Sea Level']

    fig = plt.figure()
    plt.scatter(x, y)

    # Create first line of best fit
    prediction_x= pd.Series(range(1880,2051))

    res = linregress(x, y)
    intercept = res.intercept
    slope = res.slope
    plt.plot(prediction_x, res.intercept + res.slope*prediction_x)
    plt.xlim([1880, 2050])

    # Create second line of best fit
    x2 = df['Year'][df.Year > 1999]
    y2= df['CSIRO Adjusted Sea Level'][df.Year > 1999]

    prediction_x2= pd.Series(range(2000,2051))
    res2 = linregress(x2, y2)
    intercept2 = res2.intercept
    slope2 = res2.slope
    plt.plot(prediction_x2, res2.intercept + res2.slope*prediction_x2)
    plt.xlim([1850, 2075])
    plt.ylim([0,20])

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

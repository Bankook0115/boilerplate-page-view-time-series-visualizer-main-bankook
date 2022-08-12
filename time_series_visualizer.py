import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from calendar import month_name
import datetime as dt

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
# Set index
df.set_index('date',inplace=True)
# Change date str to datetime format
df.index= pd.to_datetime(df.index)

# Clean data
# Remove Page view over Top 2.5%
mask1 = (df['value'] < df['value'].quantile(0.975))
# Remove Page view lower Bottom 2.5%
mask2 = (df['value'] > df['value'].quantile(0.025))
df = df[(mask1) & (mask2)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots( nrows=1, ncols=1,figsize=(20, 6)) 
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page views')
    ax.plot(df.index,df['value'],color='red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # import library month_name
    months = month_name[1:]
    # Create Month column by pd.Categorical
    #%B : name of the month str format
    df_bar['Months'] = pd.Categorical(df_bar.index.strftime('%B'), categories=months, ordered=True)
    # Make pivot to get right data for bar plot!
    dfp = pd.pivot_table(data=df_bar, index=df_bar.index.year, columns='Months', values='value',aggfunc='mean')
    
    # Draw bar plot
    fig = dfp.plot.bar(figsize=(8,8)).figure
    plt.xlabel('Years')
    plt.ylabel(' Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

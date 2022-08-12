import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

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
    df_filter = df[(df.index >= '2016-05') & (df.index <= '2019-12')]
    fig, ax = plt.subplots( nrows=1, ncols=1,figsize=(20, 6)) 
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page views')
    ax.plot(df_filter.index,df_filter['value'],color='red')
    fig.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





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

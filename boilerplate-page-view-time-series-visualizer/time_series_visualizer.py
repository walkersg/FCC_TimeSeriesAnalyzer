import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date', parse_dates=True)

df
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]
df

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (12, 5))
    ax.set(xlabel = 'Date',
           ylabel = 'Page Views',
           title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.plot(df['value'], color = 'red')
    fig


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df.index.month_name()
    df_bar['year'] = df.index.year
    df_bar = pd.DataFrame(df_bar.groupby(['year','month'], sort=False)['value'].mean().astype(int))
    #df_bar = df_bar.reset_index()
    df_bar = df_bar.rename(columns={'value': 'Average Page Views'})
    df_bar
    
    # Draw bar plot
    mos = ["January","February", "March", "April", "June",
           "July", "August", "September", "October", "November", "December"]
    
    fig, ax = plt.subplots(figsize = (12, 12))
    ax.set(xlabel = 'Years')
    ax = sns.barplot(data = df_bar,x = 'year', y = 'Average Page Views', hue = 'month', hue_order = mos)
    plt.show()
    
    
    
    



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    mos1 = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct', 'Nov','Dec']
    
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(df_box['month'], categories = mos1, ordered = True)
    df_box.sort_values(by='month',inplace=True)
    df_box

    # Draw box plots (using Seaborn)
    
    
    fig, axes = plt.subplots(ncols = 2, figsize = (32,10))    
    #year plot
    sns.boxplot(data = df_box, x = 'year', y = 'value', hue ='year', ax = axes[0])
    axes[0].set(title = "Year-wise Box Plot (Trend)",
                xlabel = "Year",
                ylabel = "Page Views")
    #month Plot
    sns.boxplot(data= df_box, x = 'month', y = 'value', hue = 'month', hue_order=mos1, ax = axes[1])
    axes[1].set(title = "Month-wise Box Plot (Seasonality)",
                xlabel = "Month",
                ylabel = "Page Views")
    


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

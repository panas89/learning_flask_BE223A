import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, mpld3

def compute():
    """
    Method that compute the counts of the poll options

    Ouput:
    Returns a list of the option names and a list of values
    """
    df = pd.read_csv('results.csv',header=None)
    df = df.T
    df.dropna(inplace=True)
    s = df.loc[:,0].value_counts()
    names = list(s.index)
    votes = list(s.values)

    return names, votes

def bar_plot(names, votes):
    plt.style.use('ggplot')
    fig = plt.figure(figsize=(12,6))

    bar = plt.bar(names,votes,color='b',label='votes bar chart')
    plt.xlabel('Fields')
    plt.ylabel('Vote count')
    plt.legend()

    html_text = mpld3.fig_to_html(fig)

    return html_text


'''This file might once become the collection of useful functions'''
import numpy as np




def ecdf(data):
    """compute an ECDF function, plot the values generated for
    x and y"""
    #import packages

    import matplotlib.pyplot as plt

    import seaborn as sns

    #set style defaults

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']
    sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})
    #create two arrays of (x, y) out of 2d matrix


    #variable definition

    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)

    # build the figure

    fig, ax = plt.subplots(1,1)

    _ = ax.set_xlabel("egg size")
    _ = ax.set_ylabel("ECDF")

    _ = ax.plot(x, y, marker = ".", linestyle = "none")

    plt.show()

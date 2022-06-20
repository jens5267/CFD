#!/usr/bin/env python
import string
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import pandas as pd
import os

# I assumed these were the description for each column, not sure about the rv, so maybe you should change this
NAMES = ['timestamp', 'experiment', 'perimeter', 'comparison', 'rv']
RESULTS_FOLDER = "Results"

def createOutputFolder(folderName=RESULTS_FOLDER):
    if not os.path.isdir(folderName):
        os.mkdir(folderName)

def createDataframe(experiment: str):
    # Use pandas instead of numpy to read the data in, that way you can specify the column name instead of using e.g. [0]
    df = pd.read_csv(experiment, delimiter=r"\s+", names=NAMES)
    df = df[::10] # comment this out to use all data instead of every tenth entry
    return df

def plotExperiment(df, s=240):
    plt.figure(figsize=(25, 25))
    # x-value is timestamp, for y-values, all columns are plotted at the same figure
    for row in NAMES[1:]:
        plt.scatter(df['timestamp'], df[row], s=s, alpha=0.5, label=row)
    # you could also pass the df from createDataframe as it is and reduce the amount of plots here (df = df[::10])
    plt.legend()
    return plt

def saveImage(plt, selected_experiment):
    """Saves the image in the Result folder as experiment name with png extension"""
    plt.savefig(f'Results/{selected_experiment}.png')

def main():
    rootFolder= 'BubbleData'
    bench_quantities = os.path.join(rootFolder, 'data_bench_quantities')
    selected_experiment = 'c2g2l3'
    path = os.path.join(bench_quantities, selected_experiment+'.txt')
    df = createDataframe(path)
    image = plotExperiment(df)
    saveImage(image, selected_experiment)


    print(f'Thanks for waiting. All results are in the "{RESULTS_FOLDER}" folder')

if __name__ == "__main__":
    main()


# # Additional test
# analysis = ['80x160_01','80x160_001','160x320_001'] 
# line_1 = Line2D([0,1],[0,1],color = 'red', linestyle = 'none',marker=',',markersize=5)
# line_2 = Line2D([0,1],[0,1],color = 'blue', linestyle = 'none',marker=',',markersize=5)

# # Plotting numerical data
# time_stamps_1 = [0] + [round(0.05*i,2) for i in range(1,61)]
# time_stamps_1 = [int(ele) if ele in [1,2,3] else ele for ele in time_stamps_1] 
# line_1 = Line2D([0,1],[0,1],color = 'red', linestyle = 'none', marker='o',markersize= 20, markerfacecolor="none")
# line_2 = Line2D([0,1],[0,1],color = 'blue', linestyle = 'solid')



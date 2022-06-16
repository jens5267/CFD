import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

NAMES = ["Col A", "Col B"]

def getFiles(folder:str) -> list:
    """Searches for all files in the specified folder, returns them into a list of strings"""
    files = []
    for file in os.listdir(folder):
        # Exclude separation.csv file, since it has headers
        if file == 'separation.csv':
            pass
        else:
            files.append(os.path.join(folder, file))
    files.sort()

    return list(files)


def preProcessing(files: list) -> list:
    """Checks if a file is a csv file, changes extension if necessary, returns list"""
    for file in files:
        if not file.endswith(".csv"):
            os.rename(file, file.replace("%.", "_") + '.csv')
    return files


def plotData(dataFrames:list):
    """Receives all dataframes, plots one after the other"""
    for dataFrame in dataFrames:
        dataFrame.plot(x=NAMES[0], y= NAMES[1])
        plt.show()


def Processing(files:pd.DataFrame):
    """Processes the data"""
    dfs = []
    for index, file in enumerate(files):
        if index <= 100: # for testing purposes the amount of files used is limited to 2
            print(f"Executing file {file}")
            df = pd.read_csv(file, header=None, names = NAMES, delimiter=r"\s+")
            dfs.append(df)
    return dfs

def main():
    """Main function that calls the other function to run in certain order"""
    files = getFiles('data')
    files = preProcessing(files)
    dfs = Processing(files)
    # plotData(dfs) # turn this on if you want to see the plots generated


if __name__ == "__main__":
    main()
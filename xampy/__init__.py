import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def makeCSV(filepath):
    df = pd.read_csv(filepath)
    return df

def showInfo(dataframe):
    print(dataframe.describe())
    print("-"*50)
    print(dataframe.info())


def sexBin(dataframe,genderCol):
    dataframe[genderCol] = dataframe[genderCol].map( {'female': 1, 'male': 0} ).astype(int)
    dataframe[genderCol] = dataframe[genderCol].map( {'Female': 1, 'Male': 0} ).astype(int)
    return dataframe

def numBarPlot(dataframe, items:list):
    def bar_plot(variable):
        """
            input: variable ex: "Sex"
            output: bar plot & value count
        """
        # get feature
        var = dataframe[variable]
        # count number of categorical variable
        varValue = var.value_counts()
        
        # visualize
        plt.figure(figsize = (9,3))
        plt.bar(varValue.index, varValue)
        plt.xticks(varValue.index, varValue.index.values)
        plt.ylabel("Frequency")
        plt.title(variable)
        plt.show()
        print("{}: \n {}".format(variable, varValue))

    for c in items:
        bar_plot(c)



def catPlots(dataframe,items:list):
    def plot_hist(variable):
        plt.figure(figsize = (9,3))
        plt.hist(dataframe[variable], bins = 50)
        plt.xlabel(variable)
        plt.ylabel("Frequency")
        plt.title("{} distrubution with hist".format(variable))
        plt.show()
    for n in items:
        plot_hist(n)


def countMissing(df):
    print(df.isnull().sum())

def ModeFill(dataframe,colName):
    dataframe[colName] = dataframe[colName].fillna(df[colName].mode()[0])

def MeanFill(dataframe,colName):
    dataframe[colName] = dataframe[colName].fillna(df[colName].mean().round(3))

def remove_numbers(text): 
    result = re.sub(r'\d+', '', text) 
    return result

#make a new df where a col == a certain val
def InDF(df,col,val):
    df = df[topics_data[col] == val]
    return df

#create a new df where it takes all rows where a col isnt equal
def OutDF(df,col,val):
    df = df[topics_data[col] != val]
    return df

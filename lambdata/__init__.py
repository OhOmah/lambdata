# Making a function that will check a dataframe for nulls and then print/report them
import pandas as pd 
import numpy as np 

def is_null(df):
    # Setting up my initial mask
    isnull = df.isnull()
    # Now creating the mask that will only display null values
    mask = isnull.any(axis=1)
    # Setting a new dataframe that wil contain only nulls
    df1 = df[mask]
    # Returns the count of nulls in the dataframe
    return print("there are {} null values in this dataset".format(df1.size))


def con_matrix(y_test, y_pred):
    # Importing needed libaries
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix
    # Setting my initial confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    # Naming my fig and ax for labels
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax - ax.matshow(cm)
    # Setting my labels
    plt.title('Confusion matrix of the classifier')
    fig.colorbar(cax)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()



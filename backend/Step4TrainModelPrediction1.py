## Importing the libraries
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
from joblib import dump, load
import warnings


import regression_multiLinear
import regression_polynomial
import regression_knn
import regression_decisionTree
import regression_randomForest
import regression_svrLinear
import regression_svrNonLinear
import regression_xgb



def train_model_prediction1(): 

    dataset = pd.read_csv('./Data/game_info_cleaned.csv')

    # print(dataset.head())

    dataset.isnull().values.any()

    ## Defining the features and the dependent variable
    x = dataset.iloc[:,1:0].values
    y = dataset.iloc[:,4].values
    # print(x[0])
    # print(y)


    # Retaining only the useful features of the dataset
    # From the heatmap, we can decipher that the columns NA_Sales,JP_Sales,EU_Sales and Other_Sales are the most useful features
    # in determining the global sales
    x = dataset.iloc[:,5: -3].values
    # print(x[0])

    ## Splitting the dataset into independent and dependent vaiables
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)


    path_fig = './Figure/prediction1/'
    path_model = './Model/prediction1/'


    r2_MultiLinear = regression_multiLinear.train(x_train, y_train, x_test, y_test, path_fig, path_model)
    r2_poly = regression_polynomial.train(x_train, y_train, x_test, y_test, path_fig, path_model)
    r2_knn = regression_knn.train(x_train, y_train, x_test, y_test, path_fig, path_model)
    r2_decisionTree = regression_decisionTree.train(x_train, y_train, x_test, y_test, path_fig, path_model)
    r2_randomForest = regression_randomForest.train(x_train, y_train, x_test, y_test, path_fig, path_model)
    r2_svrLinear = regression_svrLinear.train(x_train, y_train, x_test, y_test, path_fig, path_model)
    r2_svrNonLinear = regression_svrNonLinear.train(x_train, y_train, x_test, y_test, path_fig, path_model)
    r2_xgb = regression_xgb.train(x_train, y_train, x_test, y_test, path_fig, path_model)



    ## Comparing the r2 scores of different models
    labelList = ['Multiple Linear Reg.','Polynomial Reg.','K-NearestNeighbors','Decision Tree','Random Forest',
                'Linear SVR','Non-Linear SVR','XGBoost Reg.']
    mylist = [r2_MultiLinear,r2_poly,r2_knn,r2_decisionTree,r2_randomForest,r2_svrLinear,r2_svrNonLinear,r2_xgb]
    for i in range(0,len(mylist)):
        mylist[i]=np.round(mylist[i]*100,decimals=3)
    # print(mylist)


    plt.figure(figsize=(14,8))
    ax = sns.barplot(x=labelList,y=mylist)
    plt.yticks(np.arange(0, 101, step=10))
    plt.title('r2 score comparison among different regression models',fontweight='bold')
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        ax.annotate('{:.3f}%'.format(height), (x +0.25, y + height + 0.8))
    # plt.show()


    path_fig = os.path.join(path_fig, 'comparing_r2scores_differentmodels.png')
    plt.savefig(path_fig, dpi=300)

    listModel = ['regression_multiLinear', 'regression_polynomial', 'regression_knn', 'regression_decisionTree', 'regression_randomForest', 'regression_svrLinear', 'regression_svrNonLinear', 'regression_xgb']

    print("Done train model prediction 1")

    return listModel


# list = train_model_prediction1()

# print(list)
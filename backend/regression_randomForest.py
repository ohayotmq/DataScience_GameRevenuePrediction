import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump
import os


def train(x_train, y_train, x_test, y_test, path_fig, path_model):
     
    # Finding out the optimal number of trees for Random Forest Regression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score


    forestRange=range(50,500,50)
    scores_list=[]
    for i in forestRange: 
        regressor_Forest = RandomForestRegressor(n_estimators=i,random_state=0)
        regressor_Forest.fit(x_train,y_train)
        y_pred = regressor_Forest.predict(x_test)
        scores_list.append(r2_score(y_test,y_pred))
    plt.plot(forestRange,scores_list,linewidth=2,color='maroon')
    plt.xticks(forestRange)
    plt.xlabel('No. of trees')
    plt.ylabel('r2 score of Random Forest Reg.')
    # plt.show()    


    # Training the Random Forest regression on the training model
    regressor_Forest = RandomForestRegressor(n_estimators=300,random_state=0)
    regressor_Forest.fit(x_train,y_train)
    y_pred = regressor_Forest.predict(x_test)
    r2_forest = r2_score(y_test,y_pred)
    print(r2_forest)


    path_fig = os.path.join(path_fig, 'regression_randomForest.png')
    path_model = os.path.join(path_model, 'regression_randomForest.joblib')
    
    plt.savefig(path_fig, dpi=300)

    dump(regressor_Forest, path_model) 

    return r2_forest


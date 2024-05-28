import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump
import os


def train(x_train, y_train, x_test, y_test, path_fig, path_model):
    
## Finding the optimal number of neighbors for KNN regression
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.metrics import r2_score



    knnRange = range(1,11,1)
    scores_list = []
    for i in knnRange:
        regressor_knn = KNeighborsRegressor(n_neighbors=i)
        regressor_knn.fit(x_train,y_train)
        y_pred = regressor_knn.predict(x_test)
        scores_list.append(r2_score(y_test,y_pred))
    plt.plot(knnRange,scores_list,linewidth=2,color='green')
    plt.xticks(knnRange)
    plt.xlabel('No. of neighbors')
    plt.ylabel('r2 score of KNN')
    # plt.show()   


    # Training the KNN model on the training set
    regressor_knn = KNeighborsRegressor(n_neighbors=4)
    regressor_knn.fit(x_train,y_train)
    y_pred = regressor_knn.predict(x_test)
    r2_knn = r2_score(y_test,y_pred)
    print(r2_knn)


    path_fig = os.path.join(path_fig, 'regression_knn.png')
    path_model = os.path.join(path_model, 'regression_knn.joblib')
    

    plt.savefig(path_fig, dpi=300)

    dump(regressor_knn, path_model)

    return r2_knn

    


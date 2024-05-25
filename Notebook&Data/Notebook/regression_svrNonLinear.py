import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump
import os


def train(x_train, y_train, x_test, y_test, path_fig, path_model):
    
    from sklearn.metrics import r2_score

    ## Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.transform(x_test)
    sc_y = StandardScaler()
    y_train = sc_y.fit_transform(np.reshape(y_train,(len(y_train),1)))
    y_test = sc_y.transform(np.reshape(y_test,(len(y_test),1)))


    y_train = y_train.ravel()
    y_test = y_test.ravel()



    ## Training the Non-linear SVR model on the training set
    from sklearn.svm import SVR
    regressor_NonLinearSVR = SVR(kernel='rbf')
    regressor_NonLinearSVR.fit(x_train,y_train)


    ## Predicting test results
    y_pred = regressor_NonLinearSVR.predict(x_test)


    ## Calculating r2 score
    r2_NonlinearSVR = r2_score(y_test,y_pred)
    print(r2_NonlinearSVR)

   
    # path_fig = os.path.join(path_fig, 'regression_svrNonLinear.png')
    path_model = os.path.join(path_model, 'regression_svrNonLinear.joblib')
    
    # plt.savefig(path_fig, dpi=300)

    dump(regressor_NonLinearSVR, path_model) 


    return r2_NonlinearSVR


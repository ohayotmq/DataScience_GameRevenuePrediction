import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump
import os


def train(x_train, y_train, x_test, y_test, path_fig, path_model):
    ## Training the multiple linear regression on the training set
    from sklearn.linear_model import LinearRegression
    regressor_MultiLinear = LinearRegression()
    regressor_MultiLinear.fit(x_train,y_train)


    ## Predicting test results
    y_pred = regressor_MultiLinear.predict(x_test)

    # Calculating r2 score
    from sklearn.metrics import r2_score
    r2_MultiLinear = r2_score(y_test,y_pred)
    print(r2_MultiLinear)


    path_fig = os.path.join(path_fig, 'regression_multiLinear.png')
    path_model = os.path.join(path_model, 'regression_multiLinear.joblib')
    

    plt.savefig(path_fig, dpi=300)

    dump(regressor_MultiLinear, path_model) 

    return r2_MultiLinear


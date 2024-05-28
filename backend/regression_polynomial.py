import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump
import os


def train(x_train, y_train, x_test, y_test, path_fig, path_model):


    ## Finding out the optimal degree of polynomial regression
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.metrics import r2_score

    sns.set_style('darkgrid')
    scores_list = []
    pRange = range(2,6)
    for i in pRange :
        poly_reg = PolynomialFeatures(degree=i)
        x_poly = poly_reg.fit_transform(x_train)
        poly_regressor = LinearRegression()
        poly_regressor.fit(x_poly,y_train)
        y_pred = poly_regressor.predict(poly_reg.fit_transform(x_test))
        scores_list.append(r2_score(y_test,y_pred))
    plt.plot(pRange,scores_list,linewidth=2)
    plt.xlabel('Degree of polynomial')
    plt.ylabel('r2 score with varying degrees')
    # plt.show()
    
    ## Training the polynomial regression on the training model

    poly_reg = PolynomialFeatures(degree=2)
    x_poly = poly_reg.fit_transform(x_train)
    poly_regressor = LinearRegression()
    poly_regressor.fit(x_poly,y_train)
    y_pred = poly_regressor.predict(poly_reg.fit_transform(x_test))
    r2_poly = r2_score(y_test,y_pred)
    print(r2_poly)



    path_fig = os.path.join(path_fig, 'regression_polynomial.png')
    path_model = os.path.join(path_model, 'regression_polynomial.joblib')
    

    # plt.savefig(path_fig, dpi=300)

    dump(poly_regressor, path_model) 

    return r2_poly


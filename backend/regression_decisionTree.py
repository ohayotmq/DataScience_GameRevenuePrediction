import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump
import os


def train(x_train, y_train, x_test, y_test, path_fig, path_model):
    
    # Training the Decision Tree regression on the training model
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import r2_score


    regressor_Tree = DecisionTreeRegressor(min_samples_leaf=30)
    regressor_Tree.fit(x_train,y_train)


    # Predicting test results
    y_pred = regressor_Tree.predict(x_test)

    # Calculating r2 score
    r2_tree = r2_score(y_test,y_pred)
    print(r2_tree)



    path_fig = os.path.join(path_fig, 'regression_decisionTree.png')
    path_model = os.path.join(path_model, 'regression_decisionTree.joblib')
    

    plt.savefig(path_fig, dpi=300)

    dump(regressor_Tree, path_model)

    return r2_tree

    


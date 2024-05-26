from joblib import load
import numpy as np

path_model1 = '../Model/prediction1/regression_multiLinear.joblib'
path_model2 = '../Model/prediction1/regression_polynomial.joblib'
path_model3 = '../Model/prediction1/regression_knn.joblib'
path_model4 = '../Model/prediction1/regression_randomForest.joblib'
path_model5 = '../Model/prediction1/regression_decisionTree.joblib'
path_model6 = '../Model/prediction1/regression_svrLinear.joblib'
path_model7 = '../Model/prediction1/regression_svrNonLinear.joblib'
path_model8 = '../Model/prediction1/regression_xgb.joblib'

# Tải mô hình từ file 8
model = load(path_model8)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x_new = np.array([[0.000e+00, 0.000e+00, 2.900e-01, 0.000e+00, 1.200e+01, 2.008e+03]])

from sklearn.preprocessing import StandardScaler
sc_x1 = StandardScaler()
x_new = sc_x1.fit_transform(x_new)
y = model.predict(x_new)


# poly_reg = PolynomialFeatures(degree=2)
# y = model.predict(poly_reg.fit_transform(x_new))
# y = model.predict(x_new)

print("Kết quả dự đoán:", y)

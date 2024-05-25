## Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from joblib import dump, load
import warnings
warnings.filterwarnings('ignore')


dataset = pd.read_csv('../Data/game_info_cleaned.csv')

print(dataset.head())

dataset.isnull().values.any()

## Defining the features and the dependent variable
x = dataset.iloc[:,1:0].values
y = dataset.iloc[:,4].values
print(x[0])
print(y)

# Retaining only the useful features of the dataset
# From the heatmap, we can decipher that the columns NA_Sales,JP_Sales,EU_Sales and Other_Sales are the most useful features
# in determining the global sales
x = dataset.iloc[:,5: ].values
print(x[0])

## Splitting the dataset into independent and dependent vaiables
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

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

## Finding out the optimal degree of polynomial regression
from sklearn.preprocessing import PolynomialFeatures
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


plt.savefig('../Figure/regressor_multiLinear.png', dpi=300)

dump(regressor_MultiLinear, '../Model/regressor_multiLinear.joblib') 

## Training the polynomial regression on the training model
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(x_train)
poly_regressor = LinearRegression()
poly_regressor.fit(x_poly,y_train)
y_pred = poly_regressor.predict(poly_reg.fit_transform(x_test))
r2_poly = r2_score(y_test,y_pred)
print(r2_poly)


## Finding the optimal number of neighbors for KNN regression
from sklearn.neighbors import KNeighborsRegressor
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



plt.savefig('../Figure/regressor_knn.png', dpi=300)

# Training the KNN model on the training set
regressor_knn = KNeighborsRegressor(n_neighbors=7)
regressor_knn.fit(x_train,y_train)
y_pred = regressor_knn.predict(x_test)
r2_knn = r2_score(y_test,y_pred)
print(r2_knn)


dump(regressor_knn, '../Model/regressor_knn.joblib') 

# Training the Decision Tree regression on the training model
from sklearn.tree import DecisionTreeRegressor
regressor_Tree = DecisionTreeRegressor(min_samples_leaf=30)
regressor_Tree.fit(x_train,y_train)


# Predicting test results
y_pred = regressor_Tree.predict(x_test)

# Calculating r2 score
r2_tree = r2_score(y_test,y_pred)
print(r2_tree)


plt.savefig('../Figure/regressor_tree.png', dpi=300)

dump(regressor_Tree, '../Model/regressor_tree.joblib') 

# Finding out the optimal number of trees for Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
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

plt.savefig('../Figure/regressor_forest.png', dpi=300)



# Training the Random Forest regression on the training model
regressor_Forest = RandomForestRegressor(n_estimators=100,random_state=0)
regressor_Forest.fit(x_train,y_train)
y_pred = regressor_Forest.predict(x_test)
r2_forest = r2_score(y_test,y_pred)
print(r2_forest)



dump(regressor_Forest, '../Model/regressor_forest.joblib') 

## Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(np.reshape(y_train,(len(y_train),1)))
y_test = sc_y.transform(np.reshape(y_test,(len(y_test),1)))


print(x_train)
print(x_test)
print(y_test)
print(y_train)



## Training the Linear SVR model on the training set
from sklearn.svm import SVR
regressor_SVR = SVR(kernel='linear')
regressor_SVR.fit(x_train,y_train)


## Predicting test results
y_pred = regressor_SVR.predict(x_test)


## Calculating r2 score
r2_linearSVR = r2_score(y_test,y_pred)
print(r2_linearSVR)

# plt.savefig('../Figure/regressor_forest.png', dpi=300)

dump(regressor_SVR, '../Model/regressor_svr.joblib') 



## Training the Non-linear SVR model on the training set
from sklearn.svm import SVR
regressor_NonLinearSVR = SVR(kernel='rbf')
regressor_NonLinearSVR.fit(x_train,y_train)


## Predicting test results
y_pred = regressor_NonLinearSVR.predict(x_test)


## Calculating r2 score
r2_NonlinearSVR = r2_score(y_test,y_pred)
print(r2_NonlinearSVR)


dump(regressor_NonLinearSVR, '../Model/regressor_nonlinearsvr.joblib') 


# Applying XGBoost Regression model on the training set
# !pip install xgboost

from xgboost import XGBRegressor



regressor_xgb = XGBRegressor()
regressor_xgb.fit(x_train,y_train)

## Predicting test results
y_pred = regressor_xgb.predict(x_test)

## Calculating r2 score
r2_xgb = r2_score(y_test,y_pred)
print(r2_xgb)


dump(regressor_xgb, '../Model/regressor_xgb.joblib') 



## Comparing the r2 scores of different models
labelList = ['Multiple Linear Reg.','Polynomial Reg.','K-NearestNeighbors','Decision Tree','Random Forest',
             'Linear SVR','Non-Linear SVR','XGBoost Reg.']
mylist = [r2_MultiLinear,r2_poly,r2_knn,r2_tree,r2_forest,r2_linearSVR,r2_NonlinearSVR,r2_xgb]
for i in range(0,len(mylist)):
    mylist[i]=np.round(mylist[i]*100,decimals=3)
print(mylist)


plt.figure(figsize=(14,8))
ax = sns.barplot(x=labelList,y=mylist)
plt.yticks(np.arange(0, 101, step=10))
plt.title('r2 score comparison among different regression models',fontweight='bold')
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.annotate('{:.3f}%'.format(height), (x +0.25, y + height + 0.8))
# plt.show()

plt.savefig('../Figure/comparing_r2scores_differentmodels.png', dpi=300)




import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

#importing the dataset
Dataset = pd.read_csv('../Data/game_info_cleaned.csv')
#Label Encoding
from sklearn.preprocessing import LabelEncoder
number = LabelEncoder()
Dataset


Dataset['Console'] = number.fit_transform(Dataset['Console'].astype('str'))
Dataset['Genre'] = number.fit_transform(Dataset['Genre'].astype('str'))
Dataset['Publisher'] = number.fit_transform(Dataset['Publisher'].astype('str'))

#extracting the feature vector and the dependant variable vector

columns = ["Console", "Genre", "Publisher", "NA Sales (m)", "EU Sales (m)","JP Sales (m)"]


y = Dataset["Total Sales (m)"].values
X = Dataset[list(columns)].values

#importing the linear model library
from sklearn import linear_model

regr = linear_model.LinearRegression()
#importing the train test split library and splitting data into 80% for training 20% for testing
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=0)
#scaling the data 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
# apply same transformation to test data
X_test = scaler.transform(X_test)
#fit the train data to the linear model
regr.fit(X_train, y_train)

#Printing Accuracy in our Linear model
Accuracy = regr.score(X_train, y_train)
print ("Accuracy in the training data with Linear Regression Model: ", Accuracy*100, "%")

accuracy = regr.score(X_test, y_test)
print ("Accuracy in the test data with Linear Regression model", accuracy*100, "%")
#Comparing the model predicted results vs the Test set
y_pred_Model1 = regr.predict(X_test)
y_pred_Model1


compare_Model1 = np.concatenate((y_pred_Model1.reshape(len(y_pred_Model1),1), y_test.reshape(len(y_test),1)),1)
compare_Model1
####*************************
#Using DecisionTreeRegressor : 
from sklearn.tree import DecisionTreeRegressor
DTR  = DecisionTreeRegressor()
DTR2 =DecisionTreeRegressor(min_samples_leaf=0.2)
DTR3 =DecisionTreeRegressor(min_samples_leaf=15)
DTR4 =DecisionTreeRegressor(min_samples_leaf=30)
DTR5 =DecisionTreeRegressor(min_samples_leaf=35)


DTR.fit(X_train, y_train)
DTR2.fit(X_train,y_train)
DTR3.fit(X_train,y_train)
DTR4.fit(X_train,y_train)
DTR5.fit(X_train,y_train)

#printing Accuracy in our DTR Model

Accuracy = DTR.score(X_train, y_train)
print ("Accuracy in the training data with Decision Tree Regression model before tuning  : ", Accuracy*100, "%")

accuracy = DTR.score(X_test, y_test)
print ("Accuracy in the test data with Decision Tree Regression model before tuining : ", accuracy*100, "%")
##########################
Accuracy2 = DTR2.score(X_train, y_train)
print ("\nAccuracy in the training data with Decision Tree Regression model After tuning with min_samples_leaf=3 : ", Accuracy2*100, "%")

accuracy2 = DTR2.score(X_test, y_test)
print ("Accuracy in the test data with Decision Tree Regression model After tuning with min_samples_leaf=3 : ", accuracy2*100, "%")
##########################
Accuracy3 = DTR3.score(X_train, y_train)
print ("\nAccuracy in the training data with Decision Tree Regression model After tuning with min_samples_leaf=15 : ", Accuracy3*100, "%")

accuracy3 = DTR3.score(X_test, y_test)
print ("Accuracy in the test data with Decision Tree Regression model After tuning with min_samples_leaf=15 : ", accuracy3*100, "%")
##########################
Accuracy4 = DTR4.score(X_train, y_train)
print ("\nAccuracy in the training data with Decision Tree Regression model After tuning with min_samples_leaf=30 : ", Accuracy4*100, "%")

accuracy4 = DTR4.score(X_test, y_test)
print ("Accuracy in the test data with Decision Tree Regression model After tuning with min_samples_leaf=30 : ", accuracy4*100, "%")
##########################
Accuracy5 = DTR5.score(X_train, y_train)
print ("\nAccuracy in the training data with Decision Tree Regression model After tuning with min_samples_leaf=35 : ", Accuracy5*100, "%")

accuracy5 = DTR5.score(X_test, y_test)
print ("Accuracy in the test data with Decision Tree Regression model After tuning with min_samples_leaf=35 : ", accuracy5*100, "%")
##########################

#Comparing the model predicted results vs the Test set
y_pred_Model2 = DTR.predict(X_test)
y_pred_Model2

y_pred_Model2_Tuned = DTR5.predict(X_test)
y_pred_Model2_Tuned

compare_Model2 = np.concatenate((y_pred_Model2.reshape(len(y_pred_Model2),1), y_test.reshape(len(y_test),1)),1)
compare_Model2

compare_Model2_Tuned = np.concatenate((y_pred_Model2_Tuned.reshape(len(y_pred_Model2_Tuned),1), y_test.reshape(len(y_test),1)),1)
compare_Model2_Tuned
"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp import views
import os
from django.conf import settings
import threading
import globalVar
from Step1Webscraping import webScraping
from Step2DataCleaning import dataCleaning
from Step3EDA import Step3EDA
from Step4TrainModelPrediction1 import train_model_prediction1
from Step4TrainModelPrediction2 import train_model_prediction2
from Step4TrainModelPrediction3 import train_model_prediction3

urlpatterns = [
    path('', views.test),
    path('admin/', admin.site.urls),
    path('scraped-data/', views.scrapedGameData),
    path('predict-1/', views.predict1),
    path('predict-2/', views.predict2),
    path('predict-3/', views.predict3),
]

def runScheduledTask():
    # cao data va luu vao file csv
    print('runScheduledTask')
    webScraping()
    dataCleaning()
    Step3EDA()
    train_model_prediction1()
    train_model_prediction2()
    train_model_prediction3()
    globalVar.scrapedFileName = os.path.join(settings.BASE_DIR, './Data/game_info_cleaned.csv')

    # huan luyen mo hinh
    globalVar.modelFilesName1['decisionTree'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_decisionTree.joblib')
    globalVar.modelFilesName1['knn'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_knn.joblib')
    globalVar.modelFilesName1['multiLinear'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_multiLinear.joblib')
    # globalVar.modelFilesName1['polynomial'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_polynomial.joblib')
    globalVar.modelFilesName1['randomForest'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_randomForest.joblib')
    globalVar.modelFilesName1['svrLinear'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_svrLinear.joblib')
    globalVar.modelFilesName1['svrNonLinear'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_svrNonLinear.joblib')
    # globalVar.modelFilesName1['xgb'] = os.path.join(settings.BASE_DIR, 'Model/prediction1/regression_xgb.joblib')

    globalVar.modelFilesName2['decisionTree'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_decisionTree.joblib')
    globalVar.modelFilesName2['knn'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_knn.joblib')
    globalVar.modelFilesName2['multiLinear'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_multiLinear.joblib')
    # globalVar.modelFilesName2['polynomial'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_polynomial.joblib')
    globalVar.modelFilesName2['randomForest'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_randomForest.joblib')
    globalVar.modelFilesName2['svrLinear'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_svrLinear.joblib')
    globalVar.modelFilesName2['svrNonLinear'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_svrNonLinear.joblib')
    # globalVar.modelFilesName2['xgb'] = os.path.join(settings.BASE_DIR, 'Model/prediction2/regression_xgb.joblib')


    # repeat after 7 days
    threading.Timer(3600*24*7, runScheduledTask).start()

runScheduledTask()

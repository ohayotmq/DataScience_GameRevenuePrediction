from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import csv
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from sklearn.preprocessing import StandardScaler
import joblib
import globalVar
from predict3 import predict3Helper, testPredict3
from sklearn.preprocessing import PolynomialFeatures
# Create your views here.

@api_view(['GET'])
def scrapedGameData(request):
     # Read CSV file
    data = []
    with open(globalVar.scrapedFileName, newline='', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    searchText = request.GET.get('searchText')
    filtered_data = [row for row in data if any(searchText.lower() in str(value).lower() for value in row.values())]


    # Set up pagination
    paginator = PageNumberPagination()
    paginator.page_size = 10  # Number of items per page
    result_page = paginator.paginate_queryset(filtered_data, request)
    
    # Return paginated response
    return paginator.get_paginated_response(result_page)


@api_view(['GET'])
def predict1(request):
    res = {}
    x = [[float(request.GET.get('NA_sales')),float(request.GET.get('EU_sales')),
            float(request.GET.get('JP_sales')),
            # float(request.GET.get('otherSales')),
            # int(request.GET.get('releaseMonth')),int(request.GET.get('releaseYear'))
            ]]
    for modelName in globalVar.modelFilesName1:
        model = joblib.load(globalVar.modelFilesName1[modelName])
        if modelName == 'polynomial':
            poly_reg = PolynomialFeatures(degree=2)
            res[modelName] = float(model.predict(poly_reg.fit_transform(x))[0])
        elif modelName == 'xgb':
            print(modelName)
            # sc_x1 = StandardScaler()
            # x_new = sc_x1.fit_transform(x)
            res[modelName] = float(model.predict(x)[0])
        else:
            res[modelName] = model.predict(x)[0]
    return JsonResponse(res)

@api_view(['GET'])
def predict2(request):
    res = {}
    try:
        console = globalVar.consoleEncoder.transform([request.GET.get('console')])[0]
    except ValueError:
        console = -1

    try:
        genre = globalVar.genreEncoder.transform([request.GET.get('genre')])[0]
    except ValueError:
        genre = -1
    
    # try:
    #     publisher = globalVar.publisherEncoder.transform([request.GET.get('publisher')])[0]
    # except ValueError:
    #     publisher = -1
    
    x = [[console,genre,
        #   publisher,
          float(request.GET.get('NA_sales')),float(request.GET.get('EU_sales')),
          float(request.GET.get('JP_sales')),
            ]]
    for modelName in globalVar.modelFilesName2:
        model = joblib.load(globalVar.modelFilesName2[modelName])
        if modelName == 'polynomial':
            poly_reg = PolynomialFeatures(degree=2)
            res[modelName] = float(model.predict(poly_reg.fit_transform(x))[0])
        elif modelName == 'xgb':
            print(modelName)
            # sc_x1 = StandardScaler()
            # x_new = sc_x1.fit_transform(x)
            res[modelName] = float(model.predict(x)[0])
        else:
            res[modelName] = model.predict(x)[0]
    return JsonResponse(res)

@api_view(['GET'])
def predict3(request):
    # y = testPredict3(request.GET.get('genre'), request.GET.get('region'), request.GET.get('console'))
    # print(y)
    # return JsonResponse({'y':y})

    [region_max, console_max, y_max] = predict3Helper(request.GET.get('genre'), request.GET.get('region'), request.GET.get('console'))
    return JsonResponse({'region_max': region_max, 'console_max': console_max, 'revenue_max': y_max})

def test(request):
    print('ping test route')
    return HttpResponse('<div>Hi</div>')
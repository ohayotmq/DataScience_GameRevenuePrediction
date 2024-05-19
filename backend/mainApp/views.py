from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import csv
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

import globalVar
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
    
def test(request):
    print('ping test route')
    return HttpResponse('<div>Hi</div>')
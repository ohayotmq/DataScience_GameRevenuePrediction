from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import globalVar
# Create your views here.

def scrapedGameData(request):
    # tra ve tat ca data cao duoc
    if request.method == 'GET':
        # convert file csv cao duoc -> json

        fooValue = 'foo var'

        return JsonResponse({'fooKey': fooValue})
    
def test(request):
    print('ping test route')
    return HttpResponse('<div>Hi</div>')
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import json

from category.models import Category

# Create your views here.
number = 1


@csrf_exempt
def categoriesEndpointView(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)
        tree(json_data)
    return HttpResponse('Got it!')

def tree(json_data):
    if not json_data:
        return
    global number
    if type(json_data) == dict:
        while json_data.get('name'):
            print(f"{number}: {json_data.pop('name')}")
            number += 1
        if json_data.get('children'):
            transfer = json_data.pop('children')
            tree(transfer)
    elif type(json_data) == list:
        for item in json_data:
            tree(item)




def categoriesGetEndpointView(request):
    #if request.method == 'GET':
    print('What you get')
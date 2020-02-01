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
            name = json_data.pop('name')
            print(f"{number}: {name}")
            if not Category.objects.filter(name=name):
                number += 1
                obj = Category(name=name)
                obj.save()
        if json_data.get('children'):
            transfer = json_data.pop('children')
            tree(transfer)
    elif type(json_data) == list:
        for item in json_data:
            tree(item)




def categoriesGetEndpointView(request, category_id):
    answer = ''
    if request.method == 'GET':
        answer = Category.objects.get(id=category_id)
        if answer:
            print(answer)
            print('Test !!!!!!!!')
            print(backfire(category_id, answer.name))
    return HttpResponse(answer)

def backfire(category_id, etalon):
    if category_id < 1:
        return
    parents, children,siblings = [],[],[]
    last = Category.objects.last().id
    #looking for siblings and parents
    for relative_id in range(category_id - 1, 0, -1):
        relative = Category.objects.get(id=relative_id).name
        print(f"etalon == {etalon}")
        print(f"relative == {relative}")
        if relative.count('.') == etalon.count('.'):
            siblings.append(relative)
        elif relative.count('.') == etalon.count('.') - 1:
            parents.append(relative)
        #else:
        #    break
    #looking for siblings and children 
    for relative_id in range(category_id + 1, last + 1):
        relative = Category.objects.get(id=relative_id).name
        print(f"etalon == {etalon}")
        print(f"relative == {relative}")
        if relative.count('.') == etalon.count('.'):
            siblings.append(relative)
        elif relative.count('.') == etalon.count('.') + 1:
            children.append(relative)
        #else:
        #    break
    return {'parents':parents, 'siblings':siblings, 'children':children}

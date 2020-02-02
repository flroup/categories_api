from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import json
import string

from .models import Category

# Create your views here.

#Process json from POST. csrf protection is disabled
@csrf_exempt
def categoriesEndpointView(request):
    answer = None
    if request.method == "POST":
        json_data = json.loads(request.body)
        answer = tree(json_data)
    return HttpResponse(answer or 'Got it!')

#Recursion processing a json for categoriesEndpointView
def tree(json_data):
    if not json_data or "Wrong" in json_data:
        return

    
    if type(json_data) == dict:
        while json_data.get("name"):
            try:
                name,number = json_data.pop("name").split()
                print(f"{number}: {name}")
            except ValueError:
                print("Wrong format input data")
                return "Wrong format input data"
            if not name.isalpha():
                print(f"It should have only letters - {name}")
                return
            if not all([n in '.1234567890' for n in number]):
                print(f"Wrong number of tree - {number}")
            try:
                result = Category.objects.get(number=number)
            except Category.DoesNotExist:
                result = None
            if not result or not result.name == name:
    
                obj = Category(name=name, number=number)
                obj.save()
        if json_data.get("children"):
            transfer = json_data.pop("children")
            tree(transfer)
    elif type(json_data) == list:
        for item in json_data:
            tree(item)



#Answer for a request by GET on /categories/<category_id>/
def categoriesGetEndpointView(request, category_id):
    answer = result = ''
    if request.method == 'GET':
        try:
            answer = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            answer = None
        if answer:
    
            result = backfire(category_id, answer)
    
    return HttpResponse(json.dumps(result), content_type='application/json')

#Calls from categoriesGetEndpointView for process an answer for GET
def backfire(category_id, etalon):
    if category_id < 1:
        return

    parents, children, siblings = [], [], []
    txt = '.'.join(etalon.number.split('.')[:-1])
    # print(f"etalon == {etalon.number}, txt == {txt}")
    array = Category.objects.filter(name=etalon.name, number__startswith=txt)
    parray = ['.'.join(etalon.number.split('.')[0:i+1]) for i in range(etalon.number.count('.'))][::-1]
    # print(parray)
    parents = [{'id':Category.objects.get(number=relative).id, 'name':etalon.name + ' ' + Category.objects.get(number=relative).number} for relative in parray if Category.objects.filter(name=etalon.name, number=relative)]
    # print(f"parents == {parents}")
    for relative in array:
        rdot = relative.number.count('.')
        edot = etalon.number.count('.')
        
        if rdot == edot and relative.number != etalon.number:
            siblings.append({'id':relative.id, 'name': etalon.name + " " + relative.number})

        elif rdot == edot + 1 and etalon.number == relative.number[:relative.number.rfind('.')]:
            children.append({'id':relative.id, 'name': etalon.name + " " + relative.number})
    return {'id': category_id, 'name': etalon.name + ' ' + etalon.number,'parents': parents, 'children':children, 'siblings':siblings}



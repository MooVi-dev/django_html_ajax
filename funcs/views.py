import json
import time
from datetime import datetime
from pprint import pprint

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views import View
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.views.generic import FormView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer, CharField, IntegerField, BooleanField
from .forms import CheckDate


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def check_date(request):
    if request.method == "POST":
        time.sleep(2)
        userform = CheckDate(request.POST)
        if userform.is_valid():
            year = userform.cleaned_data["year"]
            return JsonResponse({'result': 'Успех!'})
        else:
            pprint(userform.hidden_error)
            return JsonResponse({'errors': userform.hidden_error})
            # return JsonResponse({'errors': })
    else:
        userform = CheckDate()
        return render(request, "check_date.html", {'form': userform})


def validate(data):
    #{ "year": 2019, "over_cur_year": 1}
    errors = []
    year = int(data['year'])
    if 'over_cur_year' in data:
        over_cur_year = data['over_cur_year']
    else:
        over_cur_year = False
    cur_year = datetime.now().year
    if year == 2018:
        errors.append('Год не должен быть равен 2018')
    elif year <= cur_year or over_cur_year:
        pass
    else:
        errors.append('Введенный год не больше текущего')
    return errors


@api_view(['POST'])
def validate_date(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        val_result = validate(data)
        print(val_result)
        if len(val_result) == 0:
            return Response({"status": "200"})
        else:
            return Response({"status": "400", "errors": val_result})
    return Response({"status": "200"})


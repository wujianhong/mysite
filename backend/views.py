# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
import json
from django.shortcuts import render
from backend.models import Employee
import pandas as pd
# Create your views here.
import numpy as np
def index(request):
    return render(request, 'home.html')

def _map(data):
    result = []

    for index, row in data.iterrows():   # 获取每行的index、row
        tmp_row = []
        for col_name in data.columns:
            tmp_row.append(row[col_name])
        result.append(tmp_row)
        print(tmp_row)
    return result

def onload(request):
    file = request.FILES.get('excel')
    df = pd.read_excel(request.FILES.get('excel'))
    print(df.items())
    print(df.columns)
    temp = _map(df)
    print(temp)

    for row in temp:
        tmp_emp = Employee(name=row[0],weight=row[1],is_trainee=row[2])
        tmp_emp.save()
    return render(request, 'excel.html')

def getEmployee(request):
    num = request.GET['num']
    emp_list = Employee.objects.filter(is_enabled=1)
    for emp in emp_list:
        emp.name
    return JsonResponse()

def excel(request):
    return render(request, 'excel.html')

def get_user(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    emp = Employee(name="吴键鸿")
    emp.save()
    return JsonResponse(name_dict)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
import json
from django.shortcuts import render
from backend.models import Employee, Person
import pandas as pd
# Create your views here.
import numpy as np
import random
import string

from datetime import datetime
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



def remove_src(li, di):
    result = li[:]
    for key in di:
        num = result.count(key)
        for i in range(num):
                # print(key, result)
            result.remove(key)
    return result

def getPerson(request):
    person_list = Person.objects.all()
    src_list = []
    for person in person_list:
        src_list.append(person.name)
    num = int(request.GET['num'])

    b = random.sample(src_list, num)
    print(type(b))
    r = list(set(b))
    tmp_list = src_list[:]
    while len(r) < num:
        tmp_list = remove_src(tmp_list, r)
        print(r, tmp_list)
        tmp_r = random.sample(tmp_list, num - len(r))
        r = list(set(r + tmp_r))
        print(r, tmp_list)
    return JsonResponse(r, safe=False)

def showNumLast(request):
    person_list = Person.objects.all()
    src_list = []
    for person in person_list:
        src_list.append(person.name)
    num = int(request.GET['num'])

    b = random.sample(src_list, num)
    print(type(b))
    r = list(set(b))
    tmp_list = src_list[:]
    while len(r) < num:
        tmp_list = remove_src(tmp_list, r)
        print(r, tmp_list)
        tmp_r = random.sample(tmp_list, num - len(r))
        r = list(set(r + tmp_r))
        print(r, tmp_list)

    for tmp in r:
        tmp_emp = Employee(name=tmp)
        tmp_emp.is_select=0
        tmp_emp.save()
    # setPesonBack()
    return JsonResponse(r, safe=False)

def reset(request):
    name_dict = {'code': 'success'}
    all_emp = Employee.objects.all()
    for tmp in all_emp:
        tmp.is_select = 1
        tmp.save()
    setPesonBack()
    return JsonResponse(name_dict)


def setPesonBack():
    Person.objects.all().delete()
    emp_list = Employee.objects.filter(is_enabled=1, is_select=1)

    for emp in emp_list:
        for i in range(emp.weight):
            tmp = Person(name=emp.name)
            tmp.save()

def setPeson(request):
    Person.objects.all().delete()
    emp_list = Employee.objects.filter(is_enabled=1, is_select=1)

    for emp in emp_list:
        for i in range(emp.weight):
            tmp = Person(name=emp.name)
            tmp.save()
    return JsonResponse({'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'})

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
    print(type(num))
    # emp_list = Employee.objects.filter(is_enabled=1)
    # for emp in emp_list:
    #     emp.name
    return JsonResponse({"name": 1})



def excel(request):
    return render(request, 'excel.html')

def get_user(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    emp = Employee(name="吴键鸿")
    emp.save()
    return JsonResponse(name_dict)

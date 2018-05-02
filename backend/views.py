# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
import json
from django.shortcuts import render
from backend.models import Employee, Person
import pandas as pd
# Create your views here.
import numpy as np
import randomimport string

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
        # print(tmp_row)    
    return result

def remove_src(li, di):    
    result = li[:]    
    for key in di:        
        num = result.count(key)        
        for i in range(num):                # print(key, result)            
            result.remove(key)    
    return result

def getPerson(request):    
    person_list = Person.objects.all()    
    src_list = []    
    for person in person_list:        
        src_list.append(person.name)    
        num = int(request.GET['num'])    
        b = random.sample(src_list, num)    
        # print(type(b))    
        r = list(set(b))    
        tmp_list = src_list[:]    
        while len(r) < num:        
            tmp_list = remove_src(tmp_list, r)        
            print(r, tmp_list)        
            tmp_r = random.sample(tmp_list, num - len(r))        
            r = list(set(r + tmp_r))        
            print(r, tmp_list)    
    return JsonResponse(r, safe=False)

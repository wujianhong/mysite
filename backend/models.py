# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)
    is_trainee = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.name

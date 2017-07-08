# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class CreateUser(models.Model):
    username = models.CharField(max_length=20, unique=False, blank=False)
    password = models.CharField(max_length=24, unique=False, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Points(models.Model):
    user = models.ForeignKey(CreateUser)
    points = models.IntegerField()

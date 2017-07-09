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
#
# class DoneTuts(models.Model):
#     user = models.ForeignKey(user)
#     One_At_A_Time = models.BooleanField(default=False)
#     Jumbler_Excercise = models.BooleanField(default=False)
#     Full_Excercise = models.BooleanField(default=False)
#     Excel_Data_Entry = models.BooleanField(default=False)
#     Selection_of_cells = models.BooleanField(default=False)
#     Simple_Data_Entry_I = models.BooleanField(default=False)
#     Simple_Data_Entry_II = models.BooleanField(default=False)
#     Cell_Size_Excercise = models.BooleanField(default=False)
#     Basic_Number_Data_Entry_Tricks = models.BooleanField(default=False)
#     Extra = models.BooleanField(default=False)
#     Current_Directory_file_upload = models.BooleanField(default=False)
#     Current_Directory_file_upload_with_specific_extension = models.BooleanField(default=False)

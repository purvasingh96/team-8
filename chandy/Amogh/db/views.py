# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

class Uploader():
    def index(self,request):
        template = loader.get_template('db/blah.html')
        context = {
            "logged_in": "loged in",
        }
        return HttpResponse(template.render(context, request))

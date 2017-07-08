# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

import random

from models import CreateUser

difficulty = [[]]
difficulty[0] = ['.DS_Store',
 '404.php',
 'advanced-search-without-map.php',
 'archive-listing-item.php',
 'archive.php',
 'blog-masonry-full-width.php',
 'blog-masonry.php',
 'blog-standard-whole-post.php',
 'blog-standard.php',
 'changes.txt',
 'comments.php',
 'footer.php',
 'full-width.php',
 'functions.php',
 'header.php',
 'index.php',
 'landing-page.php',
 'page.php',
 'product-searchform.php',
 'screenshot.png',
 'search-and-go.zip',
 'search.php',
 'searchform.php',
 'sidebar.php',
 'single-listing-item.php',
 'single-portfolio-item.php',
 'single.php',
 'slider.php',
 'style.css',
 'theme-includes.php',
 'title.php',
 'woocommerce.php',
 'wpml-config.xml']

class Uploader():

    def auth(self, request):
        if request.session.has_key('logged_in'):
            if request.session['logged_in']:
                return "Successfully logged in!"
        if request.POST.has_key("user_name") and request.POST.has_key("password"):
            user_name = request.POST['user_name']
            password = request.POST['password']
            user = CreateUser.objects.all().filter(username=user_name)
            if user[0].password == password:
                request.session['logged_in'] = True
                request.session['uid'] = user[0].pk
                return "success"
            else:
                "Incorrect Username password combination"
        else:
            return "Incorrect params"

    def index(self,request):
        if not self.auth(request):
            template = loader.get_template('db/loginpage.html')
            context = {}
            return HttpResponse(template.render(context, request))
        template = loader.get_template('db/upload.html')
        context = {
            "logged_in": "loged in",

        }


        # check if dicciculty exisits or add difficulty
        if request.GET.has_key('difficulty'):
            context['difficulty'] = request.GET['difficulty']
        else:
            context['difficulty'] = '0'


        # add file into context
        if context['difficulty'] == '0':
            context['file_name'] = random.choice(difficulty[0])
        else:
            context['file_name'] = random.choice(difficulty[0])


        # check if file has been uploaded else return fresh
        try:
            print "request.GET['datafile'] : ", request.GET['datafile']
        except Exception as e:
            return HttpResponse(template.render(context, request))



        # check the correctness of the upload
        if request.GET['datafile'] == request.GET['file_name']:
            context['correct'] = "True"
        else:
            context['correct'] = "False"

        return HttpResponse(template.render(context, request))

    def validate_auth(self,request):
        context = {}
        if not request.POST.has_key('user_name') or not request.POST.has_key('password'):
            context['messages'] = "Invalid parameters"
            template = loader.get_template('db/loginpage.html')
            return HttpResponse(template.render(context, request))
        login_param = self.auth(request)
        if login_param == self.auth(request) == 'success':
            template = loader.get_template('db/loginpage.html')
            context['messages'] = "Successfully Logged in!"
            return HttpResponse(template.render(context, request))
        else:
            context['messages'] = login_param
            template = loader.get_template('db/loginpage.html')
            return HttpResponse(template.render(context, request))

    def return_login(self,request):
        context = {}
        template = loader.get_template('db/loginpage.html')
        return HttpResponse(template.render(context, request))

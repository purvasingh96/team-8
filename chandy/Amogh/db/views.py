# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

import random

from models import CreateUser, Points

import json

import pickle

from makeform import MakeForm
m = MakeForm()
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

    def index(self, request):
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

    def validate_auth(self, request):
        context = {}
        login_param = self.auth(request)
        if login_param == 'success':
            template = loader.get_template('db/dashboard.html')
            context['messages'] = "Successfully Logged in!"
            return HttpResponse(template.render(context, request))

        else:
            context['messages'] = login_param
            template = loader.get_template('db/loginpage.html')
            return HttpResponse(template.render(context, request))

    def return_login(self, request):
        context = {'messages': " "}
        template = loader.get_template('db/loginpage.html')
        return HttpResponse(template.render(context, request))

    def logout(self, request):
        try:
            request.session['logged_in'] = False
            del request.session['uid']
        except Exception as e:
            context = {'messages': "Already Logged out"}
            template = loader.get_template('db/loginpage.html')
            return HttpResponse(template.render(context, request))

        context = {'messages': "Successfully logged out!"}
        template = loader.get_template('db/loginpage.html')
        return HttpResponse(template.render(context, request))
    def make_form(self,request):
        if request.GET.has_key('url'):
            form_rendered, form_id,ids_used = m.generate(request.GET['url'])
            pickle.dump(ids_used,open('ids_used'+form_id,"wb"))
            pickle.dump(form_rendered,open('form'+form_id,"wb"))
            context = {'form': form_rendered,'form_id':form_id,'generated':True }
            template = loader.get_template('db/standardform.html')
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('error')
    def VALIDATE_form(self,request):
        if request.GET.has_key('form_id'):
            json_gen = {}
            list_of_params = pickle.load(open('ids_used'+request.GET['form_id'],"rb"))
            try:
                for i in list_of_params:
                    json_gen[i] = request.GET[i]
            except Exception as e:
                context = {'form': pickle.load(open('form'+request.GET['form_id'])),'form_id':" " }
                template = loader.get_template('db/standardform.html')
                return HttpResponse(template.render(context, request))
            try:
                saved_json = pickle.load(open('form_data'+request.GET['form_id'],"rb"))
                saved_json.append(json_gen)
                list_of_params = pickle.dump(saved_json,open('form_data'+request.GET['form_id'],"wb"))
            except Exception as e:
                list_of_params = pickle.dump([json_gen],open('form_data'+request.GET['form_id'],"wb"))
            context = {'form': pickle.load(open('form'+request.GET['form_id'])),'form_id':" " ,"submitted":True}
            template = loader.get_template('db/standardform.html')
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('error')

    def show_data(self,request):
        if request.GET.has_key('form_id'):
            saved_json = pickle.load(open('form_data'+request.GET['form_id'],"rb"))
            params = pickle.load(open('ids_used'+request.GET['form_id'],"rb"))
            context = {"saved_json":saved_json,'form_id':" " ,"submitted":True,"params":pickle.load(open('ids_used'+request.GET['form_id'],"rb"))}
            form_content= ""
            for j in saved_json:
                form_content += "<tr>"
                for i in params:
                    form_content += "<td>"+ str(j[i]) + "</td>"
                form_content += "</tr>"
            context['table_content'] = form_content
            template = loader.get_template('db/table.html')
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('error')





class RestfulEndpoints():
    def auth(self, request):
        if request.session.has_key('logged_in'):
            if request.session['logged_in']:
                return "Already Signed in"
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

    def inc_points(self,request):
        if self.auth(request) == "Already Signed in":
            try:
                pk = request.session['uid']
                obj = CreateUser.objects.all().filter(pk=pk)
                points = Points.objects.all().filter(user=obj[0])
                p = points[0]
                points_prev_value = int(points[0].points)
                points_prev_value = points_prev_value + 1
                p.points = points_prev_value
                p.save()

            except Exception as e:
                print e

            return HttpResponse(json.dumps({"Status": "success", "message": "worked"}))

        else:
            return HttpResponse(json.dumps({"Status":"falied", "message":"no-auth"}))
            # don't do it
    def done_tuts(self,request):
        if self.auth(request) == "Already Signed in":
            if request.method == 'POST':
                got_json = request.POST['json']
                pickle.dump(got_json,open('user_'+request.session['uid'],"wb"))
                return HttpResponse(json.dumps({"status":"success"}))
            else:
                false_json = {
                "Standard_Form":False,
                "Button_Demo":False,
                "Radio_Button_Demo":False,
                "DatePicker_Demo":False,
                "CheckBoxes_Demo":False,
                "Scroll_Bar_Demo":False,
                "One_At_A_Time": False,
                "Jumbler_Excercise": False,
                "Full_Excercise": False,
                "Excel_Data_Entry": False,
                "Selection_of_cells": False,
                "Simple_Data_Entry_I": False,
                "Simple_Data_Entry_II": False,
                "Cell_Size_Excercise": False,
                "Basic_Number_Data_Entry_Tricks": False,
                "Extra": False,
                "Current_Directory_file_upload": False,
                "Current_Directory_file_upload_with_specific_extension": False
                }
                try:
                    got_jsno = pickle.load(open('user_'+request.session['uid'],"rb"))
                    return HttpResponse(json.dumps(got_jsno))
                except Exception as e:
                    pickle.dump(false_json,open('user_'+request.session['uid'],"wb"))
                    return HttpResponse(json.dumps(false_json))

        else:
            return HttpResponse(json.dumps({"Status":"falied", "message":"no-auth"}))

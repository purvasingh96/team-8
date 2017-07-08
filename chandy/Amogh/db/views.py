# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

import random

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
    def index(self,request):


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
            context['correct'] = True
        else:
            context['correct'] = False

        return HttpResponse(template.render(context, request))

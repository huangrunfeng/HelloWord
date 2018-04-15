#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    request.encoding = 'utf-8'
    if 'ac' in request.GET:
        if '1' == request.GET['tid']:  # 关于我们
            result = "about.html"
        elif '2' == request.GET['tid']:  # 解决方案
            result = "solution.html"
        elif '3' == request.GET['tid']:  # 合作品牌
            result = "partner.html"
        elif '4' == request.GET['tid']:  #
            result = "about.html"
        elif '5' == request.GET['tid']:
            result = "about.html"
        elif '6' == request.GET['tid']:
            result = "about.html"
        elif '7' == request.GET['tid']:  # 1--公司概况
            result = "about.html"
        elif '8' == request.GET['tid']:  # 1--合作品牌
            result = "about.html"
        elif '9' == request.GET['tid']:
            result = "about.html"
        elif '10' == request.GET['tid']:  # 1--联系我们
            result = "contact.html"
        else:
            result = 'index.html'
    else:
        result = 'index.html'

    return render(request, result)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # rendering HttpResponse
    # return HttpResponse('<h1> Hello World </h1>')

    name = 'Gold Nugget'
    value = 1000.00
    context = {
        'treasure_name': name,
        'treasure_val': value
    }
    return render(request, "index.html", context)
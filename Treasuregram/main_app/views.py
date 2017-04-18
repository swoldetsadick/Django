# -*- coding: utf-8 -*-
"""Treasuregram View Configuration"""
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Treasure
# from django.http import HttpResponse


# Create your views here.
def index(request):
    """ The function called when going to localhost:8888/index"""
    # rendering HttpResponse
    # return HttpResponse('<h1> Hello World </h1>')
    # When not using object class
    # name = 'Gold Nugget'
    # value = 1000.00
    # context = {
    #    'treasure_name': name,
    #    'treasure_val': value
    # }
    treasures = Treasure.objects.all()
    return render(request, "index.html", {"treasures": treasures})

"""
class Treasure:
    " This is my Treasure Class. "
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location

treasures = [
    Treasure("Gold Nugget", 500.00, "Gold", "Curly's Creek, NM"),
    Treasure("Fool's Gold", 0, "Pyrite", "Fool's Falls, CO"),
    Treasure("Coffee Can", 25.00, "Aluminium", "Acme, CA")
]
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # rendering HttpResponse
    # return HttpResponse('<h1> Hello World </h1>')
    # When not using object class
    # name = 'Gold Nugget'
    # value = 1000.00
    # context = {
    #    'treasure_name': name,
    #    'treasure_val': value
    # }
    return render(request, "index.html", {"treasures" : treasures})

class Treasure:
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
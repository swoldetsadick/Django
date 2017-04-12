# -*- coding: utf-8 -*-
"""Treasuregram main URL Configuration"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]

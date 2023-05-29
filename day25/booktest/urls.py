#!/usr/bin/python3
# 2023.05.25
from django.urls import path
from booktest import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('show_args1/<int:a>/<int:b>',views.show_args,name='show_args'),
    path('show_kwargs1/<int:c>/<int:d>',views.show_kwargs,name='show_kwargs'),
    path('url_reverse/',views.url_reverse)
]

#!/usr/bin/python3
# 2023.05.25
from django.template import Library

register = Library()

@register.filter
def mod(num,val):
    return num % val
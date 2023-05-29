"""
URL configuration for day25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the included() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booktest import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index2/',views.index2),
    path('books/',views.show_books),
    path('books/<int:bid>',views.show_heros),
    path('create/',views.create),
    path('delete/<int:bid>',views.delete),
    path('areas/',views.areas),
    path('login/',views.login),
    path('login_check/',views.login_check),
    path('test_ajax/',views.test_ajax),
    path('ajax_handle',views.ajax_handle),
    path('login_ajax/',views.login_ajax),
    path('login_ajax_check/',views.login_ajax_check),
    path('set_session/',views.set_session),
    path('get_session/',views.get_session),
    path('test_filter/',views.test_filter),
    path('test_inherit_base/',views.test_inherit_base),
    path('test_ingerit_children/',views.test_ingerit_children),
    path('verify_code/',views.verify_code),
    path('',include(('booktest.urls','booktest'),namespace='booktest')),
    path('show_upload/',views.show_upload),
    path('upload_handle/',views.upload_handle),
    path('pic_show/',views.pic_show),
    path('show_page/',views.show_page),
    path('show_area/',views.show_page),
    path('show_area/<int:pindex>/',views.show_page),
    path('tinymce',include('tinymce.urls')),
    path('editor/',views.editor),
    path('save_editor/',views.save_editor),
    path('show/',views.show)
]

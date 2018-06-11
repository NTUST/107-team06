"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

import mahoushoujyo.views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', mahoushoujyo.views.index, name='index'),
    url(r'^404notfound/', mahoushoujyo.views.notfound, name="notfound"),
    url(r'^signin/', mahoushoujyo.views.signin, name="signin"),
    url(r'^register/', mahoushoujyo.views.register, name="register"),
    url(r'^main/$', mahoushoujyo.views.main, name="main"),
    url(r'^main/hide/$', mahoushoujyo.views.hide, name="hide"),
    url(r'^main/hide/amplification/', mahoushoujyo.views.amplification, name="amplification"),
]

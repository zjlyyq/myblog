"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import blog.views as bv
import books.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^times/$', bv.current_time),
    url(r'^times/plus/(\d{1,2})/$',bv.plus_times),
    url(r'^index/$',bv.index),
    url(r'^search/$',books.views.search)
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/adddish$', views.dish, name='dish'),
    url(r'^/add$', views.add, name='dish'),
    url(r'^dummy$', views.dummy, name='dummy')
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^adddish$', views.dish, name='dish'),
    url(r'^add$', views.add, name='add'),
    url(r'^menu$', views.menu, name='menu'),
]

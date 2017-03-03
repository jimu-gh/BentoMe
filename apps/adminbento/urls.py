from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^add_dish/$', views.add_dish, name='add_dish'),
    url(r'^create_dish/$', views.create_dish, name='create_dish'),
    url(r'^add_meal/$', views.add_meal, name="add_meal"),
    url(r'^create_meal/$', views.create_meal, name="create_meal"),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^dummy/$', views.dummy, name='dummy')
]

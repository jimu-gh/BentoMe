from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^adddish$', views.dish, name='dish'),
    url(r'^login$', views.login, name='login'),
    url(r'^add$', views.add, name='add'),
    url(r'^menu$', views.menu, name='menu'),
    url(r'^dummy$', views.dummy, name='dummy'),
    url(r'^logout/$', views.logout, name='logout'),
=======
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^add_dish/$', views.add_dish, name='add_dish'),
    url(r'^create_dish/$', views.create_dish, name='create_dish'),
    url(r'^add_meal/$', views.add_meal, name="add_meal"),
    url(r'^create_meal/$', views.create_meal, name="create_meal"),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^dummy/$', views.dummy, name='dummy')
    url(r'^logout/$', views.logout, name='logout')
>>>>>>> dda89aab4df4247ced4dfdfeac154da3ab6d17ba
]

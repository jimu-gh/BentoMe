from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.login, name='login'),
    url(r'^add_dish/$', views.add_dish, name='add_dish'),
    url(r'^create_dish/$', views.create_dish, name='create_dish'),
    url(r'^add_meal/$', views.add_meal, name="add_meal"),
    url(r'^create_meal/$', views.create_meal, name="create_meal"),
<<<<<<< HEAD
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name='logout'),
=======
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^logout/$', views.logout, name='logout')
>>>>>>> f96b9f4e7c84c9cc793925e25b83ff9d7c9b0437
]

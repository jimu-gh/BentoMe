from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^show/(?P<user_id>\d+?)/$', views.show, name="show"),
    url(r'^create_feedback/$', views.create_feedback, name="create_feedback")
]

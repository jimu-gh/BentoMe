from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name="index"),
    url(r'^order_meal/(?P<meal_id>\d+?)$', views.index, name="order_meal"),
]

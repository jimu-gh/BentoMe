from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.dashboard, name="dashboard"),
    url(r'^order_meal/(?P<meal_id>\d+?)$', views.order_meal, name="order_meal")
]

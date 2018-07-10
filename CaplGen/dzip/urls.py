from django.conf.urls import url
from . import views 

app_name = "dzip"

urlpatterns = [
    url(r'^generate/$', views.generate, name="generate"),
    url(r'^$', views.index, name="index"),
]
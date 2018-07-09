from django.conf.urls import url
from . import views 

app_name = "dzip"

urlpatterns = [
    #url(r'^$', views.upload, name = "upload"),
    url(r'^$', views.index, name = "index"),
]
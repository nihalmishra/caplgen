from django.conf.urls import url
from . import views 

app_name = "dzip"

urlpatterns = [
    url(r'^$',views.main),
    #url(r'^process$',views.main,name="process"),
]
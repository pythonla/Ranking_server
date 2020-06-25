from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^upload', views.upload, name="upload"),
    url(r'^getres', views.getresult, name="getres"),
]
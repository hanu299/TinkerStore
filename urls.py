from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/$', views.email, name='email'),
    url(r'^success/$', views.success, name='success'),
]
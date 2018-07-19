from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courses$', views.index),
    url(r'^courses/new$', views.new),
    url(r'^courses/confirm_delete/(?P<id>\d+)', views.confirm_delete),
    url(r'^courses/destroy/(?P<id>\d+)', views.destroy)
]

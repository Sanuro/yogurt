from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^order$', views.order)
]                            # anticipation of all the routes that will be coming soon
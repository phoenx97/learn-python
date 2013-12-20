from django.conf.urls import patterns, url

from gothons import views

urlpatterns = patterns('',
    url(r'^$', views.start, name="start"),
)

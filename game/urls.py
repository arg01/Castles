from django.conf.urls import url

from . import views
from game.views import run_script


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    url(r'^play$', views.play, name='play'),
    url(r'^run/$', run_script, name='runscript'),
]

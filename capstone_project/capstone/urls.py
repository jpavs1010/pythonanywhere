from django.conf.urls import url
from . import views

app_name = 'capstone'
urlpatterns = [
    url(r'^map/', views.index2, name='index2'),
    url(r'^getdata/', views.getdata, name='getdata'),
    url(r'^getmetadata/', views.getmetadata, name='getmetadata'),
    url(r'^correlation/', views.correlation, name='correlation'),
    url(r'^scatterplot/', views.scatterplot, name='scatterplot'),
    url(r'^scatterplotdata/', views.scatterplot_data, name='scatterplot_data')
]

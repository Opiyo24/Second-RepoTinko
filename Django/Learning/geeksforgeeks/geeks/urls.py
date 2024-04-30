from django.urls import path
from . import views

app_name = 'geeks'

urlpatterns = [
    path('', views.index, name='index')
]
from django.urls import path
from . import views
name = 'sns_app'

urlpatterns = [
    path('', views.top, name='top'),
]
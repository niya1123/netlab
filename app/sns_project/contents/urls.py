from django.urls import path

from . import views

app_name = 'contents'

urlpatterns = [
    path('create/', views.CreateContent.as_view(), name='create_content'),
    path('create/done', views.CreateContentDone.as_view(), name='create_content_done'),
]
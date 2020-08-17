from django.urls import path

from . import views

app_name = 'contents'

urlpatterns = [
    path('content/create/', views.CreateContent.as_view(), name='create_content'),
    path('content/create/done', views.CreateContentDone.as_view(), name='create_content_done'),
    path('', views.ContentList.as_view(), name='content_list'),
]
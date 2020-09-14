from django.urls import path

from . import views

app_name = 'contents'

urlpatterns = [
    path('content/detail/<uuid:pk>/question/list', views.QuestionList.as_view(), name="question_list"),
    path('content/detail/<uuid:pk>/question/new', views.CreateQuestion.as_view(), name="add_question"),
    path('content/create/tag', views.AddTag.as_view(), name='add_tag'),
    path('content/detail/<uuid:pk>', views.ContentDetail.as_view(), name='content_detail'), 
    path('content/create/', views.CreateContent.as_view(), name='create_content'),
    path('content/create/done', views.CreateContentDone.as_view(), name='create_content_done'),
    path('', views.ContentList.as_view(), name='content_list'),
]
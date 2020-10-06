from django.urls import path

from . import views

app_name = 'contents'

urlpatterns = [
    path('content/question/delete/done', views.MyQuestionDeleteDone.as_view(), name='my_question_delete_done'),
    path('content/question/<int:pk>/delete', views.MyQuestionDelete.as_view(), name='my_question_delete'),
    path('content/question/<int:pk>/update', views.MyQuestionUpdate.as_view(), name="my_question_update"),
    path('content/<uuid:pk>/question/list', views.MyQuestionList.as_view(), name="my_question_list"),
    path('content/delete/done', views.MyContentDeleteDone.as_view(), name='my_content_delete_done'),
    path('content/<uuid:pk>/delete', views.MyContentDelete.as_view(), name='my_content_delete'),
    path('content/<uuid:pk>/update', views.MyContentUpdate.as_view(), name='my_content_update'),
    path('content/<uuid:pk>/list', views.MyContentList.as_view(), name="my_content_list"),
    path('content/detail/<uuid:content_pk>/question/list/<int:pk>/detail', views.QuestionDetail.as_view(), name="question_detail"),
    path('content/detail/<uuid:pk>/question/list', views.QuestionList.as_view(), name="question_list"),
    path('content/detail/<uuid:pk>/question/new', views.CreateQuestion.as_view(), name="add_question"),
    path('content/create/tag', views.AddTag.as_view(), name='add_tag'),
    path('content/detail/<uuid:pk>', views.ContentDetail.as_view(), name='content_detail'), 
    path('content/create/', views.CreateContent.as_view(), name='create_content'),
    path('content/create/done', views.CreateContentDone.as_view(), name='create_content_done'),
    path('', views.ContentList.as_view(), name='content_list'),
]
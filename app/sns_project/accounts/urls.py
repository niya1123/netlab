from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('user_create/', views.UserCreate, name='user_create'),
    path('user_create/done', views.UserCreateDone, name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete, name='user_create_complete'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
]
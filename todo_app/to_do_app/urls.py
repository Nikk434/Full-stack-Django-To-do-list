from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('delete/<str:name>/', views.deleteTask, name='delete'),
    path('complete/<str:name>/', views.completeTask, name='complete'),
]
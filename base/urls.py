from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='LOGIN'),
    path('logout/', views.logoutUser, name='LOGOUT'),
    path('register/', views.registerPage, name='REGISTER'),
    path('', views.home, name="HOME"),
    path('room/<str:pk>/', views.room, name="ROOM"),
    path('UserProfile/<str:pk>/', views.UserProfile, name="USERPROFILE"),
    path('createRoom/', views.createRoom, name="CREATEROOM"),
    path('updateRoom/<str:pk>/', views.updateRoom, name="UPDATEROOM"),
    path('deleteRoom/<str:pk>/', views.deleteRoom, name="DELETEROOM"),
    path('deleteMessage/<str:pk>/', views.deleteMessage, name="DELETEMESSAGE"),
    path('updateUser/', views.updateUser, name="UPDATEUSER"),
    path('topics/', views.topicsPage, name="TOPICS"),
    path('activity/', views.activityPage, name="ACTIVITY"),
]
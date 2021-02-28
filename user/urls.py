from django.contrib import admin
from django.urls import path
from user import views
app_name = "user"

urlpatterns = [
    path('register/', views.registerPage, name="registerPage"),
    path('delete/<int:id>', views.userDelete, name="userDelete"),
    path('login/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutPage, name="logoutPage"),
    path('follow/<int:id>', views.followUser, name="followUser"),
    path('unfollow/<int:id>', views.unfollowUser, name="unfollowUser"),
    path('dashboard/', views.dashboardPage, name="dashboardPage"),
    path('settings/', views.settingsPage, name="settingsPage"),
    path('<str:username>/', views.userProfile, name="userProfile"),
]

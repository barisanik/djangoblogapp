from django.contrib import admin
from django.urls import path
from article import views
app_name = "article"

urlpatterns = [
    path('detail/<int:id>', views.articleDetailPage, name="articleDetailPage"),
    path('addarticle/', views.addArticlePage, name="addArticlePage"),
    path('all/', views.allArticlePage, name="allArticlePage"),
]
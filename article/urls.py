from django.contrib import admin
from django.urls import path
from article import views
app_name = "article"

urlpatterns = [
    path('detail/<int:id>', views.articleDetailPage, name="articleDetailPage"),
    path('addarticle/', views.addArticlePage, name="addArticlePage"),
    path('edit/<int:id>', views.editArticlePage, name="editArticlePage"),
    path('delete/<int:id>', views.deleteArticlePage, name="deleteArticlePage"),
    path('all/', views.allArticlePage, name="allArticlePage"),
    path('upvote/<int:id>', views.articleUpvote, name="articleUpvote"),
]

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name="indexPage"), #Base directory
    path('about/', views.aboutPage, name="about"),
    path('article/<int:id>', views.articleDetailPage, name="article"),
    path('articles/', include("article.urls")), # Adding article/.. directories
    path('user/', include("user.urls")), # Adding user/.. directories
]

"""TestBlogDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name="indexPage"), #Kök dizin '/' ile değil '' ile ifade edilir.
    path('about/', views.aboutPage, name="about"),
    path('article/<int:id>', views.articleDetailPage, name="article"),
    path('articles/', include("article.urls")), #Eğer articles ile başlayan bir dizin istenirse article dosyasındaki urls dosyasını yükle.
    path('user/', include("user.urls")),
]

#from _typeshed import ReadableBuffer
from django.contrib import auth
from article import views
from user import views
from django.shortcuts import render, redirect, get_object_or_404

import user
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from article.models import Article # Article tablosu article uygulamasından alındı.

# Create your views here.
def registerPage(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid(): #Clean metodu burada çalışır.
        regUsername = form.cleaned_data.get("username")
        regPassword = form.cleaned_data.get("password")
        regMail = form.cleaned_data.get("email")
        newuser = User(username = regUsername, email = regMail)
        newuser.set_password(regPassword)
        newuser.save()
        login(request, newuser)
        messages.success(request, "Başarıyla kayıt oldunuz.")
        return redirect("indexPage")
    context = {
        "form" : form
    }
    return render(request,"register.html", context)

def userDelete(request, id):
    userInfo = User.objects.filter(id = id).first()
    if userInfo:
        if (userInfo.is_superuser != 1) and (userInfo != request.user):
            userInfo.delete()
            messages.success(request, "Kullanıcı başarıyla silindi.")
            return redirect("indexPage")
        else:
            messages.info(request, "İşlem başarısız.")
            return redirect("indexPage")
    else:
        messages.warning(request, "Kullanıcı bulunamadı.")
    return redirect("indexPage")

def loginPage(request):
    form = LoginForm(request.POST or None)
    context = {
    "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password= password)
        if user is None:
            messages.info(request, "Belirtilen kullanıcı bulunamadı. {}".format(user))
            return render(request, "login.html", context)
        messages.success(request, "Başarıyla giriş yaptınız.")
        login(request, user)
        return redirect("indexPage")
    return render(request, "login.html", context)

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Başarıyla çıkış yapıldı.")
        return redirect("indexPage")
    else:
        messages.info(request,"Herhangi açık bir oturum bulunamadı.")
        return redirect("indexPage")

def dashboardPage(request):
    userArticles = Article.objects.filter(author = request.user)
    context = {'articles':userArticles}
    return render(request, "dashboard.html", context)

def userProfile(request, username):
    user = get_object_or_404(User, username = username)
    #user = User.objects.filter(username = username).first()
    if user:
        if user == request.user: #Eğer profil giriş yapan kullanıcıya ait ise
            article = Article.objects.filter(author = user)
            context = {'user':user,
                        'article':article}
            return render(request, "userprofile.html",context)
        else: #Eğer profil giriş yapan başka kullanıcı ise
            article = Article.objects.filter(author = user, is_public = 1) # Herkese açık makaleleri getir.
            context = {'user':user,
                        'article':article}
            return render(request, "userprofile.html",context)
    
    else:
        messages.info(request,"Belirtilen profil bulunamadı.")
        return redirect("indexPage")

def settingsPage(request):
    return render(request, "usersettings.html")
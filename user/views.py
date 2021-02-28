from django.contrib import auth
from article import views
from user import views
from django.shortcuts import render, redirect, get_object_or_404
from user.models import UserFollow
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from article.models import Article
# 

def registerPage(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid(): 
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
            messages.info(request, "Belirtilen kullanıcı bulunamadı.")
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
    
def followUser(request,id):
    getUser = get_object_or_404(User, id=id)
    if getUser:
        checkFollow = UserFollow.objects.filter(followerID = request.user.id, personID = getUser.id).first()
        if checkFollow:
            messages.info(request, "Bu kullanıcıyı zaten takip ettiniz.")
            return redirect("indexPage")
        else:
            if (getUser != request.user):
                newFollow = UserFollow(followerID = request.user.id, personID = getUser.id)
                newFollow.save()
                messages.success(request, "{} adlı kullanıcıyı başarıyla takip ettiniz!".format(getUser.username))
                return redirect("indexPage")
            else:
                messages.info(request, "Kendinizi takip edemezsiniz.")
                return redirect("indexPage")
    else:
        messages.info(request, "Takip etmeye çalıştığınız kullanıcı bulunamadı.")
        return redirect("indexPage")
    
    
def unfollowUser(request,id):
    getUser = get_object_or_404(User, id=id)
    checkFollow = UserFollow.objects.filter(followerID = request.user.id, personID = getUser.id).first()
    if checkFollow:
        checkFollow.delete()
        messages.warning(request, "{} adlı kullanıcı takipten çıkarıldı.".format(getUser.username))
        return redirect("indexPage")
    else:
        messages.info(request, "Bir sorun oluştu. Lüten daha sonra tekrar deneyin.")
        return redirect("indexPage")
    
def dashboardPage(request):
    userArticles = Article.objects.filter(author = request.user)
    context = {'articles':userArticles}
    return render(request, "dashboard.html", context)

def userProfile(request, username):
    user = get_object_or_404(User, username = username)
    if user:
        if user == request.user: 
            article = Article.objects.filter(author = user)
            context = {'user':user,
                        'article':article}
            return render(request, "userprofile.html",context)
        else: 
            article = Article.objects.filter(author = user, is_public = 1) 
            followCheck = UserFollow.objects.filter(followerID = request.user.id, personID = user.id).first()
            context = {'user':user,
                        'article':article,
                        'follow' : followCheck}
            return render(request, "userprofile.html",context)
    else:
        messages.info(request,"Belirtilen profil bulunamadı.")
        return redirect("indexPage")

def settingsPage(request):
    return render(request, "usersettings.html")

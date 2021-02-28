import article
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from article.models import Article
#
def indexPage(request):
    return render(request,"index.html")

def aboutPage(request):
    return render(request, "about.html")

def gunluk(request): # Development diary url
    return render(request, "gunluk.html")

def articleUpvote(request, id):
    getArticle = get_object_or_404(Article, id=id)
    checkupvote = getArticle.votes.exists(request.user.id)
    if checkupvote:
        getArticle.votes.delete(request.user.id)
    else:
        getArticle.votes.up(request.user.id)
    url = '/articles/detail/' + str(id)
    return HttpResponseRedirect(url)

def addArticlePage(request):
    form = ArticleForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla oluşturuldu!")
        return redirect("indexPage")
    return render(request, "addarticle.html", context)

def deleteArticlePage(request,id):
    getArticle = get_object_or_404(Article, id=id)
    if getArticle.author == request.user:
        getArticle.delete()
        messages.success(request,"Makale başarıyla silindi.")
        return redirect("indexPage")
    else:
        messages.info(request,"Bu işlem için yetkiniz bulunmamaktadır.")
        return redirect("indexPage")
    
def editArticlePage(request,id):
    getArticle = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = getArticle)
    if form.is_valid():
        article = form.save(commit=False) 
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla güncellendi!")
        return redirect("indexPage")
    return render(request,"editarticle.html", {"form" : form})
    
def articleDetailPage(request,id):
    getArticle = get_object_or_404(Article, id=id)
    if getArticle:
        if (getArticle.is_public == 1) or (getArticle.author == request.user):
            checkupvote = getArticle.votes.exists(request.user.id)
            context = {'article':getArticle,
                        'upvote':checkupvote}
            return render(request, "articledetails.html",context)
        else:
            messages.info(request,"Belirtilen makaleye erişim izniniz bulunmamaktadır.")
            return redirect("indexPage")
    else:
        messages.info(request,"Belirtilen makale bulunamadı.")
        return redirect("indexPage")

def allArticlePage(request):
    getAllArticles = Article.objects.filter(is_public = 1).all()
    if article:
        context = {'article' : getAllArticles}
        return render(request, "allarticles.html",context)
    else:
        messages.info(request,"Blogda makale bulunamadı.")
        return redirect("indexPage")

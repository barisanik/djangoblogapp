import article
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .forms import ArticleForm # Article Form
from django.contrib import messages
from article.models import Article # Article model

# Create your views here.
def indexPage(request):
    return render(request,"index.html")
def aboutPage(request):
    return render(request, "about.html")

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

def articleDetailPage(request,id):
    getArticle = get_object_or_404(Article, id=id)
    if getArticle:
        if (getArticle.is_public == 1) or (getArticle.author == request.user):
            context = {'article':getArticle}
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

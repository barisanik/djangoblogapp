from django.contrib import admin
from .models import Article # Article model

# Register your models here.
# This is for adding article model into admin dashboard
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "author"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article

from django.contrib import admin
from .models import Article 
#.models denmesinin sebebi admin dosyasının 
# bulunduğu dizinde bulunan models dosyasından Article
# classına erişir.

# Register your models here.
@admin.register(Article) # modeli admin panelinde erişilebilir hale getirir. decorator şeklinde yazılınca özelleştirilebilir
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "author"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta: #Django yapısıyla alakalı. ArticleAdmin ile normal article modelini birleştirir.
        model = Article

#Şimdi settings dosyasında INSTALLED APPS kısmına Article app'ini ekleyelim.
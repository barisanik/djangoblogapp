from django.db import models


# Create your models here. Tablolar

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name="Yazar") 
    # on_delete User tablosundaki kullanıcı silindiğinde makalelerini de siler
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    is_public = models.BooleanField(default=1, verbose_name="Makale gizliliği herkese açık olarak kalsın.")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi") #Anlık zamanı alır.
    # Bu veri tabanını admin py dosyasında kaydediyoruz.
    def __str__(self):
        return self.title
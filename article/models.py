from django.db import models

#
class Article(VoteModel, models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name="Yazar") 
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    is_public = models.BooleanField(default=1, verbose_name="Makale gizliliği herkese açık olarak kalsın.")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    last_edit_date = models.DateTimeField(auto_now=True, verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.title

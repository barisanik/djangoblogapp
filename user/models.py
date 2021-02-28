from django.db import models

# Create your models here.
class UserFollow(models.Model):
    id = models.AutoField(primary_key=True)
    followerID = models.CharField(max_length=10, verbose_name="Takip Eden")
    personID = models.CharField(max_length=10, verbose_name="Takip Edilen")
    follow_date = models.DateTimeField(auto_now_add=True, verbose_name="Follow Date")

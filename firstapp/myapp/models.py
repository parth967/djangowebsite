from django.db import models

# Create your models here.
class userdetail(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    class Meta:
        db_table="userdetail"

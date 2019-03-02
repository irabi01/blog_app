from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add =True)
    body = models.TextField()
    # add in thumbail later
    # add in author later
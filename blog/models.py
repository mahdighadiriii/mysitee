from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,models.SET_NULL,null=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField()
    #tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publishead_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    udated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
        


from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #author 
    #image
    title = models.CharField(max_length=100)
    content = models.TextField()
    #tag
    #category
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publishead_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    udated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
        
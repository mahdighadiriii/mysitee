from django.contrib import admin
from blog.models import Post
from django.db import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    #list_display = ('title','counted_views','status','publishead_date')
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title','content']
admin.site.register(Post,PostAdmin)


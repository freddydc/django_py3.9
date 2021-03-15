from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """docstring for ArticleAdmin"""


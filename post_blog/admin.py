from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostHomeAdmin(admin.ModelAdmin):
    pass

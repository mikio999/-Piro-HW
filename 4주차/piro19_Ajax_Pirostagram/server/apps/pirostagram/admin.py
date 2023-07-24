from django.contrib import admin
from .models import MyReddit, Comment

# Register your models here.
admin.site.register(MyReddit)
admin.site.register(Comment)
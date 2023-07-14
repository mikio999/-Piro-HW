from django.contrib import admin
from .models import myText

class MyTextAdmin(admin.ModelAdmin) :
    list_display = ('pk', 'title')
    
admin.site.register(myText)


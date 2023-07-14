from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model) :
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200 ,  null="True")
    genre = models.CharField(max_length=200,  null="True")
    star_rate = models.CharField(max_length=200 ,  null="True")
    img_url = models.CharField(max_length=200)
    board_text = RichTextUploadingField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
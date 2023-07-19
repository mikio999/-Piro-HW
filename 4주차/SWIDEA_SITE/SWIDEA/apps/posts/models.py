from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyDev(models.Model) :
    name = models.CharField('이름', max_length=200)
    kind = models.CharField('종류', max_length=200)
    content = models.TextField('내용')

    def __str__(self):
        return self.name

class MyIdea(models.Model) : 
    title = models.CharField('아이디어명', max_length=200)
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField('내용')
    interest_rate = models.IntegerField('관심도')
    devtool = models.ForeignKey(MyDev, verbose_name="예상 개발툴", on_delete=models.CASCADE, related_name='post')
    liked_by = models.ManyToManyField(User, verbose_name="찜한 사용자", blank=True, related_name="liked_idea")


    def __str__(self):
        return self.title



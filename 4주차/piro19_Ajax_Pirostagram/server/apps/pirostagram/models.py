from django.db import models

# Create your models here.

class MyReddit(models.Model) :
    title = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    like_rate = models.IntegerField('관심도')

    def __str__(self):
        return self.title
    
    
class Comment(models.Model) :
    reddit = models.ForeignKey(MyReddit, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.comment
      
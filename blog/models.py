from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title  = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})    


#All post can have more than one category and All categories have more that one post
class category(models.Model):
    name = models.CharField(max_length=45)
    posts = models.ManyToManyField(Post)

    def __str__(self) -> str:
        return self.name
    
    



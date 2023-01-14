from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# All post can have more than one category and All categories have more that one post
class Category(models.Model):
    categories = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Health', 'Health'),
        ('Personal ', 'Personal '),
        ('Political', 'Political'),
        ('Fashion', 'Fashion'),

    ]

    name = models.CharField(choices=categories, default="Food", max_length=10)
    slug = models.SlugField()
    posts = models.ManyToManyField(Post)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

# TODO: Categoryinin url ve list view oluştur.

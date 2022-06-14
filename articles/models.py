from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    thumb = models.ImageField(default='image.png', blank=True)
    likes = models.ManyToManyField(User, related_name='article_like')
    dislikes = models.ManyToManyField(User, related_name='article_dislike')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:20] + '... read more'

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()


class Person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.body[:5]}"

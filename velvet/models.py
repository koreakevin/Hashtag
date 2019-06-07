from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/' ,blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
       return self.comment_text

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name       


# Create your models here.

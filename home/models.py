from django.db import models


class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    news_url = models.URLField(max_length=250)
    title = models.CharField(max_length=150)
    content_html = models.TextField()
    summary = models.CharField(max_length=250)
    image = models.ImageField()
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    attachments = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


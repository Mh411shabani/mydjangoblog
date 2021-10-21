from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # in add tumbnail
    # add in outhor
    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body)>= 50:
            return self.body[:50] + " ..."
        else:
            return self.body[:]
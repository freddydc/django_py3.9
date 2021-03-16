from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"my_id": self.id})

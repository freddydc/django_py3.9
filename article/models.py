from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    ### Get absolute "url", use de fefault method:
        ## "get_absolute_url(self): pass"

    def get_absolute_url(self):
        # Nota: Dirige la vista a "article-detail".
        return reverse("articles:article-detail", kwargs={"my_id": self.id})

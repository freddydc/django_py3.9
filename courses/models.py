from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title}"

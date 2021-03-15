from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField(
        blank=True, 
        null=True, 
        default='Escribe la descripcion.'
    )
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0.99)
    message = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        default='Escribe un mensaje.'
    )

    def __str__(self):

        return f"Titulo: {self.title}"

    ## The method to get absolute url: --> UNO  ##
        # def get_absolute_url(self): ...
    
    # def get_absolute_url(self):
    #     return f"/my_post/{self.id}/"
    
    ## Get URLs with reverse method: --> DOS ##
        # Add NAME defined in URLS, path(..., name='my_post_url_view'), to reverse("...", ...).
        # Arguments, ID name defined in:
            # URLS path('my_post<int:my_id>/', ...) PATH 
            # VIEWS def(..., my_id): ARGUMENT
            # Add the ID name as KEY in kwargs DICTIONARY.
    ## Modelo inicial: --> UNO ##
    # def get_absolute_url(self):
        # return reverse("my_post_url_view", kwargs={'my_id': self.id})
    ## Modelo mejorado: --> DOS ##
        # Add defined name_app = 'my_post' in post_blog app urls.
    def get_absolute_url(self):
        return reverse("my_post:my_post_url_view", kwargs={'my_id': self.id})

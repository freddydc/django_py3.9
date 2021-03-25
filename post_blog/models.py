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

    ### The method to "GET ABSOLUTE URL": --> UNO:
        ## def get_absolute_url(self): pass, modelo inicial.
    
    # def get_absolute_url(self):
    #     return f"/my_post/{self.id}/"
    
    ### Get URLs with "REVERSE" method: --> DOS:

        ## Arguments, "ID" name defined in:
            # First "argument" add "name = post_url_view" defined in urls file.
            # ID: Urls path('my_post<int:my_id>/', ...)
            # VIEWS FILE: def(..., my_id): pass, set "my_id" argument.
            # Add the "ID" name as "KEY" in "kwargs" DICTIONARY.

    ### Modelo inicial "REVERSE": --> UNO
    # def get_absolute_url(self):
        # return reverse("post_url_view", kwargs={'my_id': self.id})

    ## Modelo mejorado "REVERSE": --> DOS
        # Add defined name_app = 'my_post' in post_blog app urls.
    def get_absolute_url(self):
        return reverse("my_post:post_url_view", kwargs={'my_id': self.id})

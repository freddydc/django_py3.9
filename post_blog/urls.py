from django.urls import path
from post_blog import views
# from post_blog.views import *

### Define app_name, para diferenciar de otras URLs:
    # app_name= 'Custom Name'
app_name = 'my_post'

urlpatterns = [
    ### Dynamic url to link click view ... ###
        ## Modelo inicial:
    # path('my_post/', views.my_post_url, name='my_post_url'),
    # path('my_post/<int:my_id>/', views.my_post_url_view, name='my_post_url_view'),
        ## Modelo mejorado:
    path('my_post/', views.my_post_url, name='my_post_url'),
    path('my_air/<int:my_id>/', views.my_post_url_view, name='my_post_url_view'),
    ### END: Dynamic url to link click view ... ###
]

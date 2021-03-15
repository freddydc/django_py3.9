from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)

app_name = 'articles'

urlpatterns = [
    ## pk <=> id, pk is required por defecto: '<int:pk>/', for views based in CLASS. ##
        ## Para utilizar "id", create a function in views.
    path('', ArticleListView.as_view(), name='article-list'),
    ## Url default, acepta "pk" ##
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    ## Url mejorado, para aceptar "id"  ##
    path('<int:my_id>/', ArticleDetailView.as_view(), name='article-detail'),
]

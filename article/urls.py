from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
)

app_name = 'articles'

urlpatterns = [
    ### pk <=> id, pk is required por defecto: '<int:pk>/', for class views:
        ## Para utilizar "id", create a function in specific view.
    path('list/', ArticleListView.as_view(), name='article-list'),
        ## DetailView, url default, acepta "pk".
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
        ## DetailView, url mejorado, para aceptar "id".
    path('detail/<int:my_id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
]

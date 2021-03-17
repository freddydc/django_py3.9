from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

# Nota: The name for get URLs.
app_name = 'articles'

urlpatterns = [
    ### pk <=> id, "pk" is required por defecto: '<int:pk>/', for "class" views:
        ## Para utilizar "id", create a function in specific view.
    path('list/', ArticleListView.as_view(), name='article-list'),
        ## DetailView, url default, acepta "pk".
    ### path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
        ## DetailView, url mejorado, para aceptar "id".
    path('detail/<int:my_id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:my_id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:my_id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]

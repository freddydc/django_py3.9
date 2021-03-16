from django.shortcuts import render, get_object_or_404
from .forms import ArticleModelForm
from .models import *
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your class views based here.


class ArticleCreateView(CreateView):

    template_name = 'my_articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, my_form):
        print(f"Form cleaned data: {my_form.cleaned_data}\n")
        return super().form_valid(my_form)


class ArticleListView(ListView):

    ### ListView -> Notas:
        ## Name by default, para hacer referencia a template y objecto:
            # "template_name" is default:
            # "queryset" is default.

    template_name = 'my_articles/my_article_list.html'
    queryset = Article.objects.all()
    print(f"ListView queryset: {queryset}\n")


class ArticleDetailView(DetailView):

    ### DetailView -> Notas:
        ## "pk" es utilizado por defecto en queryset, para hacer referencia a objectos desde template.

    template_name = 'my_articles/article_detail.html'

    ### Method ONE:
        ## Don't need "queryset", with "get_object" function.
    # queryset = Article.objects.all()
    # print(f"DetailView queryset: {queryset}\n")

    ### Method TWO:
        ## Use "filter", and use "<int:pk>/" in urls:
            # id "id__gt=1", para hacer referencia a objetos con "id" > 1.
    # queryset = Article.objects.filter(id__gt=1)

        ## Crear una funcion para utilizar "id", para hacer referencia...
            # The "get_object", function is default:
                # Use get_object_or_404, with the def "get_object". 

    ### Don't use this function with a "filter".
    def get_object(self):
        ## Use underscore later "id_" variable, para evitar confilcts with keywords
        id_ = self.kwargs.get("my_id")
        print(f"Get id in class view: {id_}")
        return get_object_or_404(Article, id=id_)

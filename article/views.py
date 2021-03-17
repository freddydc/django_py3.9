from django.shortcuts import render, get_object_or_404
from .forms import ArticleModelForm
from django.urls import reverse
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

    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    ### Si el form es procesado con exito, dirige a la vista principal:
        ## En lugar de dirigir a la vista by default, "article-detail".
    # success_url = '/'

    ### "LEARN" more about the "form_valid", function:
        ## The function "return", a cleaned data from form:
            # In dictionary format for use before.

    def form_valid(self, my_form):
        print(f"\nFORM CLEANED DATA: {my_form.cleaned_data}\n")
        return super().form_valid(my_form)

    # def get_succes_url(self):
    #     return '/'


class ArticleListView(ListView):

    ### ListView -> Notas:
        ## Name by default, para hacer referencia a template y objecto:
            # "template_name" is default:
            # "queryset" is default.

    template_name = 'article/my_article_list.html'
    queryset = Article.objects.all()
    print(f"LISTVIEW QUERYSET: {queryset}\n")


class ArticleDetailView(DetailView):

    ### DetailView -> Notas:
        ## "pk" es utilizado por defecto en queryset. Para utilizar en templates.

    template_name = 'article/article_detail.html'

    ### Method ONE:
        ## Don't need "queryset", with "get_object" function.

    queryset = Article.objects.all()
    print(f"DETAILVIEW QUERYSET: {queryset}\n")

    ### Method TWO:
        ## Use "filter", and use "<int:pk>/" in urls:
            # id "id__gt=1", para hacer referencia a objetos con "id" > 1.

    # queryset = Article.objects.filter(id__gt=1)

        ## Crear una funcion para utilizar "id".
            # The "get_object", function is default:
                # Use get_object_or_404, with the def "get_object". 

    ### Don't use this function with a "filter".
    def get_object(self):
        ## Use underscore later "id_" variable, para evitar confilcts with keywords
        id_ = self.kwargs.get("my_id")
        print(f"GET ID IN CLASS VIEW: {id_}")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):

    template_name = 'article/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        ## Nota: get_object_or_404(<Nombre de model>, <Campos del model> = <data>)
        return get_object_or_404(Article, id=id_)

    def form_valid(self, my_id):
        return super().form_valid(my_id)


class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'
    ### Delete View, need the module: "reverse"

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PostForm, RawPostForm
from .models import Post

# Create your views here.


def home_main(request):

    ## Quuery Set:
        # List of objects.
    queryset = Post.objects.all()

    # Recibe request of user logged.
    print(f"Request of user: {request.user}")
    ## Recibe complete url request.
    print(f"Request url: {request}")

    user_req = request.user

    name = ['freddy', 'felipe', 'juan', 'pedro']
    lastname = ['diaz', 'castane', 'russell', 'tylor']
    title = 'the first project'
    paragraph = "<p> Es un parrafo desde views.py </p>"

    context = {
        'names': name,
        'lastname': lastname,
        'user': user_req,
        'title': title,
        'prf': paragraph,
        # queryset
        'object_list': queryset,
    }

    return render(request, 'main.html', context)


### DYNAMIC URL TO LINK ###

def my_post_url(request):

    queryset = Post.objects.all()

    context = {
        'object_list': queryset,
    }

    return render(request, 'main.html', context)


def my_post_url_view(request, my_id):
    try:
        obj = Post.objects.get(id=my_id)
    except Post.DoesNotExist:
        raise Http404

    data = {
        'object': obj,
    }

    return render(request, 'blog_post/dynamic.html', data)

### END DYNAMIC URL TO LINK ###


# def home_post(request, name, age):
def home_post(request):

    print(f"Request of user: {request.user}")
    print(f"Request url: {request}")

    # name = name
    # age = age

    # return HttpResponse(f"<p>Hola {name} que tal, tu edad es {age}</p>")

    return render(request, 'post_blog/post.html')


def blog_store(request):

    obj = Post.objects.get(id=1)

    data = {
        'title': obj.title,
        'details': obj.details,
    }

    return render(request, 'blog_post/details.html', data)

## FORMULARIOS ##

### Metodo 1:
    # Formulario uno

def form_create_view(request):

    my_form = PostForm(request.POST or None)

    print(f"\nmy_form es: {my_form}\n")

    if my_form.is_valid():

        my_form.save()
        my_form = PostForm()

        print(f"Formulario: {my_form}\n")

    context = {
        'form': my_form,
    }

    return render(request, 'post_blog/form_create_view.html', context)


### Metodo 2:
    # Formulario dos

def form_create_url(request):

    ## For get method example:
        # <== View example: ==>
            # localhost:8000/form_url/?title=a title here
    print(f"\nForm req GET: {request.GET} \nForm req GET (title): {request.GET['title']} \nForm req POST: {request.POST}\n")

    if request.method == 'POST':
        my_title = request.POST.get('title')

        print(f"my_title metodo GET ('title'): {my_title}\n")
        # Use this instruction for create new title:
        # Post.objects.create(title=my_title)

    data = {}

    return render(request, 'post_blog/form_create_url.html', data)


### Metodo 3:
    # Formulario tres

def form_create_raw(request):
    
    ### Metodo uno:

        # No aparece que el campo es obligatario.
    # my_form = RawPostForm()

        # Aparece que el campo es obligatario con metodo POST.
    # my_form = RawPostForm(request.POST)

    ### Metodo dos:

    my_form = RawPostForm()
    print(f"my_form before: {my_form}")

    # Recibe la peticion POST para el formulario.
    if request.method == "POST":
        my_form = RawPostForm(request.POST)
        print(f"\nmy_form later: {my_form}\n")

        # Verifica por completo que el formulario es valido.
        if my_form.is_valid():
            # Now the data is good.
            print(f"Form is valid: {my_form.cleaned_data}\n")

            ### SAVE FORM IN BASE DATA:
                # Utilizar doble "*" (**name...) para pasar argumentos KEY, VALUE.
            Post.objects.create(**my_form.cleaned_data)

            print(f"Get form for save: {Post.objects.create(**my_form.cleaned_data)}\n")

        else:
            print(f"Form isn't valid: {my_form.errors}\n")

    data = {
        'form': my_form,
    }

    return render(request, 'post_blog/form_create_raw.html', data)

## END: FORMULARIOS ##


def template_app(request):

    obj = Post.objects.get(id=1)

    data = {
        'title': obj.title,
        'details': obj.details,
    }

    return render(request, 'post_blog/post_template.html', data)


def account_view(request, *args, **kwargs):

    print(f"*args: {args}, **kwargs: {kwargs}")

    # return HttpResponse('<p>Hola usuario</p')
    return render(request, 'post_blog/account.html')


def render_initial_data(request):

    # Forma inicial:
    initial_data = {
        'title': 'My awesome title',
    }

    my_obj = Post.objects.get(id=1)

    ## RawForm:
    # form = RawPostForm(request.POST or None, initial=initial_data)

    ## ModelForm:
        # Conflict with arguments, don't set (my_obj) object:
            # ... , initial=initial_data, instance=my_obj ...

    # form = PostForm(request.POST or None, initial=initial_data, instance=my_obj)
        # This method set default instance of my_obj:
            # ... , instance=my_obj ...
    form = PostForm(request.POST or None, instance=my_obj)

    if form.is_valid():
        form.save()

    print(f"Form: {form}")

    context = {
        'form': form,
    }

    return render(request, 'post_blog/form_initial_data.html', context)


### Dynamic url get objects:
    ## Hacer referencia a objetos desde URL.

def dynamic_lookup_view(request, my_id):

    ### Uno:
        ## Set manual id:
            # Se define un unico ID para hacer referencia al objecto.
    # obj = Post.objects.get(id=1)

    ### Dos:
        ## Set id by url:
            # Se pasa un numero por url para obtener el objeto.
    # obj = Post.objects.get(id=my_id)

    ### Tres GET_OBJECT_OR_404:
        ## Handle doesn't exist: Use module get_object_or_404:
            # Se encarga de mostrar error 404, si no enecuentra el objeto con su ID.
    # obj = get_object_or_404(Post, id=my_id)

    ### Cuatro HTTP404:
        ## Se encarga de mostrar error 404, si no enecuentra el objeto con su ID:
            # Use Http404 module:
                # ... try: pass
                # .. except: pass
    try:
        obj = Post.objects.get(id=my_id)
    except Post.DoesNotExist:
        raise Http404

    data = {
        'object': obj,
    }

    return render(request, 'blog_post/dynamic.html', data)


### Delete data Objects

def post_delete_data(request, my_id):

    obj = get_object_or_404(Post, id=my_id)
    ## POST request delete data

    if request.method == 'POST':
        ## Confirming delete
        obj.delete()
        ## Use redirect module:
            # Redirect module dirige a otra vista despues de ejecutar.
            # ... redirect('../../')
        return redirect('http://localhost:8000/')

    data = {
        'object': obj,
    }

    return render(request, 'post_blog/delete_data.html', data)

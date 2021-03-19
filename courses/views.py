from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm


### HTTP Methods
def my_home(request, *args, **kwargs):

    print(f"VIEW THE REQUEST METHOD IN THE 'DEF VIEW': {request.method}\n")

    return render(request, 'course/my_home.html', {})


### Base View Class = View
class CourseView(View):
    ### Notas: 
        ## The "self" is required in "get()" function. The "self", is useful in class.
        ## In the class "View", based views the "template_name", not is a standar.

    template_name = 'course/my_home.html'

    def get(self, request, *args, **kwargs):
        ## "GET" method
        print(f"\nTHE REQUEST METHOD IN THE 'CLASS VIEW': {self.request.method}\n")

        return render(request, self.template_name, {})

    def post(request, *args, **kwargs):
        ## "POST" method
        print(f"\nTHE REQUEST METHOD IN THE 'CLASS VIEW': {self.request.method}\n")

        return render(request, 'course/my_home.html', {})


### RAW DETAIL CLASS BASED IN "View" MODULE
class CourseDetailView(View):

    template_name = 'course/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):

        data = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            ## Create a "KEY" and "VALUE", for data dictionary
            data['object'] = obj
            print(f"\nMY DATA: {data}\n")

        return render(request, self.template_name, data)


### RAW LIST CLASS BASED IN "View" MODULE
class CourseListView(View):

    template_name = 'course/course_list.html'
    queryset = Course.objects.all()

    ### Create a custom funcion to get a "queryset".
    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):

        data = {
            ### Metodo UNO: sin funcion "get_queryset(self): pass".
            # 'object_list': self.queryset,
            ### Metodo DOS: with the function "get_queryset(self): pass".
            'object_list': self.get_queryset(),
        }

        return render(request, self.template_name, data)

### HEREDAR DE VISTA "CourseListView"
class MyCourseListView(CourseListView):
    queryset = Course.objects.filter(id=1)


### RAW CREATE CLASS BASED "View" MODULE
class CourseCreateView(View):
    ### Notas:
        ## This view need a "form".

    template_name = 'course/course_create.html'

    ### GET Method
    def get(self, request, *args, **kwargs):

        form = CourseModelForm()
        data = {
            'form': form,
        }

        return render(request, self.template_name, data)

    ### GET Method
    def post(self, request, *args, **kwargs):
        ### Raw validation on a "POST METHOD", forms file.
        form = CourseModelForm(request.POST)

        if form.is_valid():
            form.save()
            ### Despues de guardar, limpia el formulario a "GET METHOD"
            form = CourseModelForm()

            print(f"\nBEFORE COMPLETE FORM CLEAN: {form}\n")

        data = {
            'form': form,
        }

        return render(request, self.template_name, data)


### RAW UPDATE CLASS BASED IN "View" MODULE
class CourseUpdateView(View):

    template_name = 'course/course_update.html'

    ### Create a function to get "id".
    def get_objet(self):

        id = self.kwargs.get('id')
        obj = None
        print(f"\nGET ID WITH KWARGS: {id}\n")

        if id is not None:
            obj = get_object_or_404(Course, id=id)

        return obj

    ### GET method
    def get(self, request, id=None, *args, **kwargs):

        data = {}
        ### Set the value defined in "get_object(self)" function.
        obj = self.get_objet()
        print(f"GET METHOD OBJECT: {obj}\n")

        if obj is not None:
            ### Set the object "obj", obtained to instance
            form = CourseModelForm(instance=obj)
            data['object'] = obj
            data['form'] = form

        return render(request, self.template_name, data)

    ### POST method
    def post(self, request, id=None, *args, **kwargs):

        data = {}
        obj = self.get_objet()
        print(f"POST METHOD OBJECT: {obj}\n")

        if obj is not None:
            ### Set the object "obj", obtained to instance, and request "POST".
            form = CourseModelForm(request.POST, instance=obj)

            if form.is_valid():
                form.save()

            data['object'] = obj
            data['form'] = form

        return render(request, self.template_name, data)


### RAW DELETE CLASS BASED IN "View" MODULE
class CourseDeleteView(View):

    template_name = 'course/course_delete.html'

    def get_object(self):

        id = self.kwargs.get('id')
        obj = None

        if id is not None:
            obj = get_object_or_404(Course, id=id)

        return obj

    def get(self, request, id=None, *args, **kwargs):

        data = {}
        obj = self.get_object()

        if obj is not None:
            data['object'] = obj

        return render(request, self.template_name, data)

    def post(self, request, id=None, *args, **kwargs):

        data = {}
        obj = self.get_object()

        if obj is not None:
            obj.delete()
            data['object'] = None

            return redirect('/courses/list/')

        return render(request, self.template_name, data)


### CUSTOM MIXIN FOR CLASS BASED IN "View" MODULE

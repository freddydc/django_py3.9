from django.shortcuts import render
from django.views import View
from .models import Course


### Base View Class = View
class CourseView(View):
    ### Notas: 
        ## The "self" is required in "get()" function. The "self", is useful in class.
        ## In the class "View", based views the "template_name", not is a standar.

    template_name = 'course/my_fav.html'

    def get(self, request, *args, **kwargs):
        ## "GET" method
        print(f"\nVIEW THE REQUEST METHOD IN THE 'CLASS VIEW': {self.request.method}\n")
        return render(request, self.template_name, {})

    def post(request, *args, **kwargs):
        ## "POST" method
        print(f"\nVIEW THE REQUEST METHOD IN THE 'CLASS VIEW': {self.request.method}\n")
        return render(request, 'course/my_fav.html', {})


### HTTP Methods
def my_favourite(request, *args, **kwargs):

    print(f"VIEW THE REQUEST METHOD IN THE 'DEF VIEW': {request.method}\n")
    return render(request, 'course/my_fav.html', {})

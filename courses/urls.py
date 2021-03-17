from django.urls import path
from courses.views import (
    my_favourite,
    CourseView,
)

# Nota: Mi url app name.
app_name = 'my_courses'

urlpatterns = [
    path('', CourseView.as_view(template_name='main/details.html'), name='course-list'),
    path('list/', my_favourite, name='courses-list'),
]

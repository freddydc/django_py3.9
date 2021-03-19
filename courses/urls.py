from django.urls import path
from courses.views import (
    my_home,
    CourseView,
    CourseDetailView,
    CourseListView,
    MyCourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

# Nota: Mi url app name.
app_name = 'courses'

urlpatterns = [
    path('home/', my_home, name='courses-home'),
    path('', CourseView.as_view(), name='courses-list'),
    ### Modelo mejorado: Set another "template_name", defined in the "View".
    path('set/', CourseView.as_view(template_name='main/details.html'), name='courses-list'),
    path('<int:id>/detail/', CourseDetailView.as_view(), name='my_courses-detail'),
    path('list/', CourseListView.as_view(), name='my_course_list'),
    ### This view hereda de "CourseListView"
    path('my_list/', MyCourseListView.as_view(), name='my_course_list_heredado'),
    ### Create new object, using formulary
    path('create/', CourseCreateView.as_view(), name='my_course_create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='my_course_update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='my_course_delete'),
]

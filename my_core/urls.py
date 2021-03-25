"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from post_blog import views
# from post_blog.views import *

urlpatterns = [
    ### The admin URL
    path('admin/', admin.site.urls),
    # path('post/<str:name>/<str:age>/', views.post_view, name='post_view')
    ### MAIN TEMPLATE VIEW
    path('', views.post_main, name='home'),
    path('store/', views.blog_store, name='store'),
    path('post_view/', views.post_view, name='post_view'),
    path('user/', views.post_account, name='account'),
    path('post_detail/', views.post_details, name='post_detail'),
    ### END: MAIN TEMPLATE VIEW
    ### FORMULARIOS
        ## for_url: localhost:8000/form_url/?title=sublime
    path('form_view/', views.form_view, name='form_view'),
    path('form_url/', views.form_url, name='form_url'),
    path('form_raw/', views.form_raw, name='form_raw'),
    ### END: FORMULARIOS
    ### Render Initial Data
    path('render_data/', views.render_init_data, name='render_init_data' ),
    ### END: Render Initial Data
    ### Add urls, de apps
    path('post_blog/', include('post_blog.urls')),
    path('article/', include('article.urls')),
    path('courses/', include('courses.urls')),
    ### END: Add urls, de apps
    ### Dynamic url to link click view
    # path('my_post/', views.my_post_url, name='post_url'),
    # path('my_view/<int:my_id>/', views.my_post_url_view, name='post_url_view'),
    ### END: Dynamic url to link click view
    ### Set same name='post_url', URLs to get a problem with same "name".
    path('profile/<int:my_id>/', views.post_account, name='post_url'),
    ### END: Set same name='post_url', URLs to get a problem with same "name".
    ### Argument "my_id" in process for use in menu "NAVIGATION"
    path('dynamic/<int:my_id>/', views.dynamic_lookup_view, name='dynamic'),
    path('del/<int:my_id>/del/', views.post_delete_data, name='delete_data'),
    ### END: Argument "my_id" in process for use in menu "NAVIGATION"
]

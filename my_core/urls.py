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
    path('admin/', admin.site.urls),
    # path('post/<str:name>/<str:age>/', views.home_post, name='post')
    ### MAIN TEMPLATE VIEW ###
    path('', views.home_main, name='home'),
    path('store/', views.blog_store, name='store'),
    path('post/', views.home_post, name='blog'),
    path('account/', views.account_view, name='account'),
    path('template_app/', views.template_app, name='template_app'),
    ### END: MAIN TEMPLATE VIEW ###
    ### FORMULARIOS ###
        ## localhost:8000/form_air/?title=django
    path('form_create_view/', views.form_create_view, name='form_create_view'),
    path('form_url/', views.form_create_url, name='form_url'),
    path('form_create_raw/', views.form_create_raw, name='form_create_raw'),
    ### END: FORMULARIOS ###
    ### Render Initial Data ###
    path('render_init_data/', views.render_initial_data, name='render_init_data' ),
    ### END: Render Initial Data ###
    ### Add urls, de apps ###
    path('post_blog/', include('post_blog.urls')),
    path('article/', include('article.urls')),
    ### END: Add urls, de apps ###
    ### Dynamic url to link click view ... ###
    # path('my_post/', views.my_post_url, name='my_post_url'),
    # path('my_post/<int:my_id>/', views.my_post_url_view, name='my_post_url_view'),
    ### END: Dynamic url to link click view ... ###
    ### Create same <- name='...' ->, URLs to generate a problem with same URLs ###
    path('cuenta/<int:my_id>/', views.account_view, name='my_post_url_view'),
    ### END: Create same <- name='...' ->, URLs to generate a problem with same URLs ###
    ### Argument MY_ID en proceso para utilizar en menu NAVIGATION... ###
    path('dynamic/<int:my_id>/', views.dynamic_lookup_view, name='dynamic'),
    path('delete/<int:my_id>/delete/', views.post_delete_data, name='delete_data'),
    ### END: Argument MY_ID en proceso para utilizar en menu NAVIGATION... ###
]

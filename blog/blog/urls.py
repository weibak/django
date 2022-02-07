"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from blog.views import register, sign_in, logout_view
from posts import views
from posts.views import posts_index_2, create_post, post_list, post_list_all
from profiles.views import profiles_index, search_profile
from shop.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list,),
    path('index2/', posts_index_2,),
    path('search_slug/', views.search_slug,),
    path('search_title/', views.search_title),
    path('search_posts/', views.search_user_posts),
    path('profiles/', profiles_index, ),
    path('profile_profile/', search_profile, ),
    path('register/', register, name='register'),
    path('auth/', sign_in, name="auth"),
    path('post/', create_post, name="post_add"),
    path("api/", include("api.urls", namespace="api")),
    path('logout/', logout_view, name='logout'),
    path('posts/all/', post_list_all, name='posts_all'),
    path('products/all/', product_list, name='product_all'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

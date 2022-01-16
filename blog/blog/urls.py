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
from django.contrib import admin
from django.urls import path

from posts.views import posts_index, posts_index_2
from photos.views import blog1_index, blog1_index_2, post_r

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', posts_index,),
    path('index2/', posts_index_2,),
    path('blogind/', blog1_index,),
    path('blogind2/', blog1_index_2),
    path('postr/', post_r),

]

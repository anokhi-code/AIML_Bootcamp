"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from library.views import AuthorView, BookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', AuthorView.as_view({'get': 'list', 'post': 'create'},name='author-list-create')),
    path('author/<int:pk>/', AuthorView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'},name='author-detail')),
    path('book/', BookView.as_view({'get': 'list', 'post': 'create'},name='book-list-create')),
    path('book/<int:pk>/', BookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'},name='book-detail')),
]

"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from webapp import views as webapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp_views.index_view, name='index'),
    path('product/new/', webapp_views.product_create_view, name='product_create'),
    path('product/<int:pk>/', webapp_views.product_view, name='product_detail'),
    path('product/<int:pk>/edit/', webapp_views.product_update_view, name='product_update'),
    path('product/<int:pk>/delete/', webapp_views.product_delete_view, name='product_delete'),
    path('cat_list/', webapp_views.category_list_view, name='category_list'),
    path('cat/', webapp_views.category_create, name='category_new'),
    path('cat/<int:pk>/edit/', webapp_views.category_edit, name='category_edit'),
    path('cat/<int:pk>/delete/', webapp_views.category_delete, name='category_delete'),
]

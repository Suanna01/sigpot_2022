"""sigpotprj URL Configuration

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
    2. Add a URL to urlpatterns:  path('post/', include('post.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from sigpotapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),

    path('login/', accounts_views.login, name="login"),
    path('logout/', accounts_views.logout, name="logout"),
    path('signup/', accounts_views.signup, name="signup"),

    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('board/', views.board, name='board'),
    path('detail/<int:post_id>', views.create_comment, name="create_comment")
]

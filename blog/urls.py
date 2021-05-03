from django.urls import include, path

from .views import PostTitle, PostDetail, UpdatePost, DeletePost
from . import views

urlpatterns = [
    path('user/', views.profile, name="profile"),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name = "register"),
    path('post/delete/<int:pk>/', DeletePost.as_view(), name = "delete"),
    path('post/update/<int:pk>/', UpdatePost.as_view(), name = "edit"),
    path('post/new/', views.create, name="new"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post"),
    path('', PostTitle.as_view(), name="home"),
]

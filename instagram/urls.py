from django.urls import path 
from . import views
from .views import ImageListView, ImageCreateView, ImageDeleteView, ImageDetailView, UserImageListView

urlpatterns = [

    path('register/', views.register, name ='register'),
    path('profile-update/', views.profile, name='profile'),
    path('user/<str:username>', UserImageListView.as_view(), name='user-posts'),
    path('post/<int:pk>/delete/', ImageDeleteView.as_view(), name='post-delete'), 
    path('post/new', ImageCreateView.as_view(), name= 'post-create'),
    path('post/<int:pk>/delete', ImageDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', ImageDetailView.as_view(), name='post-detail'),
    path('',views.homepage , name='home'),
    path('like/', views.like_image, name='like_image'),
    path('search/', views.search_results, name='search_results')
    


]
from django.urls import path
from . import views

urlpatterns = [ 
<<<<<<< HEAD
    path('', views.home_page, name='home-page'),
    path('posts/', views.all_posts, name='all-posts'),
    path('posts/<slug:slug>/', views.blog_post, name='blog-post'),
=======
    path('', views.PostTempelateView.as_view(), name='home-page'),
    path('posts/', views.PostListView.as_view(), name='all-posts-page'),
    path('read_later/', views.ReadLaterView.as_view(), name='read-later'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-page'),
    
>>>>>>> 0eb7a81 (Blog Website Up and Running)
]
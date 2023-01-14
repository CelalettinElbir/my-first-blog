from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,CategoryDetailView

urlpatterns = [
    
    path('',PostListView.as_view(),name = 'blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name = 'user-posts'),
    path('about/',views.about,name = 'blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'),

    # path("category/<slug:slug>",CategoryListView.as_view(),name="categories"),
    path("<slug:slug>",CategoryDetailView.as_view(),name="category-posts"),

]

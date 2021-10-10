from django.urls import path
from .views import AddPostView, like, UserPostListView, PostListView, SearchView
urlpatterns = [
    path('addpost/', AddPostView.as_view(), name='add_post_url'),
    path('like/<int:id>/', like, name='like_url'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user_post_list_url'),
    path('search/', SearchView.as_view(), name='search_url'),
    path('', PostListView.as_view(), name='post_list_url'),
]
from django.contrib import admin
from django.urls import path
from webapp.views import UserListView, UserDetailView, ArticleListView, ArticleDetailView, UserFavoritesView, ArticleCreateView, \
    ArticleUpdateView, CommentCreateView, UpdateCommentView, ArticleDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('users', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('favorites/<int:pk>', UserFavoritesView.as_view(), name='user_favorites'),
    path('article/create', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/create_comment', CommentCreateView.as_view(), name='article_com_create'),
    path('article/<int:pk>/update_comment', UpdateCommentView.as_view(), name='article_com_update'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
]
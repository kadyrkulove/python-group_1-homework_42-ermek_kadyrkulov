from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from webapp.models import User, Article, Comment, Rating
from webapp.forms import ArticleForm
from django.urls import reverse_lazy, reverse


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'



class UserFavoritesView(DetailView):
    model = User
    template_name = 'user_favorites.html'

class ArticleCreateView(CreateView): #Задание из 3 домашки
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')
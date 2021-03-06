from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from webapp.models import User, Article, Comment, Rating
from webapp.forms import ArticleForm, UpdateCommentForm, CommentForm, ArticleSearchForm
from django.urls import reverse_lazy, reverse


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return self.model.objects.filter(title__icontains=article_name)
        else:
            return self.model.objects.all()

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

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'article_com_create.html'
    form_class = CommentForm
    success_url = reverse_lazy('article_detail')

    def form_valid(self, form):
        form.instance.article = get_object_or_404(Article, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})

class UpdateCommentView(UpdateView):
    model = Comment
    template_name = 'article_com_update.html'
    form_class = UpdateCommentForm
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


from django import forms
from webapp.models import Article, Comment

class ArticleSearchForm(forms.Form):
    article_name = forms.CharField(max_length=100, required=False, label="Заголовок")

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'commented_by']

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        exclude = ['article', 'commented_by', 'parent_comment']
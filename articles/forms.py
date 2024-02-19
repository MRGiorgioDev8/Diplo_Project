from django import forms
from .models import Article, Comment, Bookmark, Category
from tinymce.widgets import TinyMCE


class ArticleForm(forms.ModelForm):
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), label='Categories')
    class Meta:
        model = Article
        fields = ['title', 'content', 'photo', 'categories']
        widgets = {
            'content': TinyMCE(attrs={'class': 'content_edit'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': TinyMCE(attrs={'class': 'content_comment'}),
        }

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['user', 'article']


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'photo']
        widgets = {
            'content': TinyMCE(attrs={'class': 'content_edit'}),
        }
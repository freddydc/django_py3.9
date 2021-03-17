from django import forms
from .models import Article


# Model Form form class view.
class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]

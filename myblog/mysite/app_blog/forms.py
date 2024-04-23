from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(label='Фото', widget=forms.FileInput(), help_text='Максимум 250 символів', required=False)

    class Meta:
        model = ArticleImage
        fields = ['image', 'title']

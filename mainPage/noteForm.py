from django import forms
from blog.models import Post


class createNoteForm(forms.Form):

    title = forms.CharField(max_length=40, label='', widget=forms.TextInput(
        attrs={'class': 'form-control m-form', 'placeholder': 'Заголовок'},))
    text = forms.CharField(max_length=500,  label='', widget=forms.TextInput(
        attrs={'class': 'form-control m-form', 'placeholder': 'Описание', }))
    tags = forms.CharField(max_length=30, required=False, label='', widget=forms.TextInput(
        attrs={'class': 'form-control m-form', 'placeholder': 'Теги', }))
    category = forms.ChoiceField(
        choices=Post.categoryPost, label="", widget=forms.Select({'class': 'custom-select', "category": "Note"}))

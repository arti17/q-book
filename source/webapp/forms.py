from django import forms
from django.forms import widgets


class EntryForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Author')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(required=True, widget=widgets.Textarea, label='Text')


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=40, required=True, label='Search')

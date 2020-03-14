from django import forms
from webapp.models import File


class FileForm(forms.ModelForm):
    class Meta:
        model=File
        exclude = ['create']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class CommonFileForm(forms.ModelForm):
    class Meta:
        model=File
        exclude=['access']


class SearchUserForm(forms.Form):
    user_search = forms.CharField(max_length=150,label='Поиск пользователя')

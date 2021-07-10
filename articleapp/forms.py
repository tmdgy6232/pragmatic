from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # medium editor를 적용하기위해 class명 커스터마이징
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'height:auto; text-align:left;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'image', 'project','content']


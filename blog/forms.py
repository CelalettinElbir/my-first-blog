from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class CategoryCreateModel(forms.ModelForm):
    # categories = [
    #     ('Food', 'Food'),
    #     ('Travel', 'Travel'),
    #     ('Health', 'Health'),
    #     ('Personal ', 'Personal '),
    #     ('Political', 'Political'),
    #     ('Fashion', 'Fashion'),

    # ]
    categories = forms.ModelMultipleChoiceField(queryset=models.Category.objects.all())
    # categories = forms.MultipleChoiceField(choices=categories)
    class Meta:
        model = models.Post
        fields = ('title', 'content',)
    
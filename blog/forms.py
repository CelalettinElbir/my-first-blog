from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class CategoryCreateModel(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(queryset=models.Category.objects.all())
    # categories = forms.MultipleChoiceField(choices=categories)
    class Meta:
        model = models.Post
        fields = ('title', 'content',)
    
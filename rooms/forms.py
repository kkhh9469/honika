from django import forms
from . import models


class SearchForm(forms.Form):

    title = forms.CharField(required=False)
    creater = forms.CharField(required=False)
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

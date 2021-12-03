
from django import forms
from . import variable as var

class FileUpload(forms.Form):
    file = forms.FileField(required=False)
    url = forms.URLField(required=False)
    category = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=var.CATEGORIES, initial='0')

class SelectColumns(forms.Form):
    columns = forms.ChoiceField(required=True)
from django import forms
from . import variable as var

class FileUpload(forms.Form):
    # file = forms.FileField(required=True, widget=forms.widgets.FileInput)
    category = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=var.CATEGORIES, initial='0')

class SelectColumns(forms.Form):
    columns = forms.ChoiceField(choices=var.CATEGORIES, required=True)

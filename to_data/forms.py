
from django import forms
from . import variable as var
from django.contrib.admin import widgets
import os

class FileUpload(forms.Form):
    file = forms.FileField(required=False)
    url = forms.URLField(required=False)
    category = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=var.CATEGORIES, initial='0')
    encode = forms.fields.ChoiceField(
        choices=(
            ('utf-8', 'utf-8'),
            ('shift_jis', 'shift_jis')),
            required = True,
            widget = forms.widgets.RadioSelect,
            initial = 'utf-8')

class SelectColumns(forms.Form):
    columns = forms.ChoiceField(required=True, initial='0')

class FileName(forms.Form):
    csv_file = forms.CharField(required=False)
    rdf_file = forms.CharField(required=False)
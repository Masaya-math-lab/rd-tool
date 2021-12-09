from django.views import generic
from django.shortcuts import render
from .forms import FileUpload
from .forms import SelectColumns
from .forms import FileName
from . import variable as var
import csv,io
import pandas as pd
import numpy as np
from .functions import to_csv
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.method == 'POST':
        if 'upload' in request.POST:
            # カテゴリーに対応するDATASETを呼び出す
            select_form = SelectColumns()
            select_form.fields['columns'].choices = var.DATASET[request.POST['category']]
            # "ThisComputer"
            if request.FILES.get('file'):
                df = pd.read_csv(io.StringIO(request.FILES['file'].read().decode('utf-8')), delimiter=',')
                col = df.columns.values.tolist()
                df = df.fillna('')
                df_list = df.to_numpy().tolist()
                context = {
                    'category': request.POST['category'],
                    'file': df.to_html(),
                    'form': select_form,
                    'df': df_list,
                    'col': col
                }
                return render(request, 'processing.html', context)

            # "Web Addressed(URLs)"
            elif request.POST['url']:
                df = pd.read_csv(request.POST['url'])
                col = df.columns.values.tolist()
                df_list = df.to_numpy().tolist()
                context = {
                    'category': request.POST['category'],
                    'file': df.to_html(),
                    'form': select_form,
                    'df': df_list,
                    'col': col
                }
                return render(request, 'processing.html', context)

        if 'select' in request.POST:
            context = {
                'form': FileName,
                'df': request.POST['df'],
                'col': request.POST['col'],
                'select_col': request.POST.getlist('columns')
            }
            return render(request, 'download.html', context)

        if 'create' in request.POST:
            if request.POST['csv_file']:
                form = FileName()
                form.fields['csv_file'].initial = request.POST['csv_file']
                context = {
                    'file_name': request.POST['csv_file'],
                    'form': form,
                    'df': request.POST['df'],
                    'col': request.POST['col'],
                    'select_col': request.POST['select_col']
                }
                return render(request, 'download.html', context)
            elif request.POST['rdf_file']:
                form = FileName()
                form.fields['rdf_file'].initial = request.POST['rdf_file']
                context = {
                    'file_name': request.POST['rdf_file'],
                    'form': form,
                    'df': request.POST['df'],
                    'col': request.POST['col'],
                    'select_col': request.POST['select_col']
                }
                return render(request, 'download.html', context)

        if 'download' in request.POST:
            list = eval(request.POST['df'])
            col = eval(request.POST['select_col'])
            df = pd.DataFrame(data=list, columns=col)
            file_name = request.POST['file_name']

            # json形式に変換する処理

            response = to_csv(df, file_name)
            return response

    else:
        upload = FileUpload
        return render(request, "index.html", {'form': upload})


'''
class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = FileUpload

    def form_valid(self, form):
        if 'upload' in self.request.POST:
            # カテゴリーに対応するDATASETを呼び出す
            select_form = SelectColumns()
            select_form.fields['columns'].choices = var.DATASET[form.cleaned_data['category']]

            # "ThisComputer"のとき
            if form.cleaned_data['file']:
                df = pd.read_csv(io.StringIO(self.request.FILES['file'].read().decode('utf-8')), delimiter=',')
                col = df.columns.values
                context = {
                    'category': form.cleaned_data['category'],
                    'col': col,
                    'file': df.to_html(),
                    'form': select_form
                }
                return render(self.request, 'processing.html', context)

            # "Web Addressed(URLs)"のとき
            elif form.cleaned_data['url']:
                df = pd.read_csv(self.request.POST['url'])
                col = df.columns.values
                context = {
                    'category': form.cleaned_data['category'],
                    'col': col,
                    'file': df.to_html(),
                    'form': select_form
                }
                return render(self.request, 'processing.html', context)

        if 'select' in self.request.POST:
            context = {
                'columns': form.cleaned_data['columns']
            }
            return render(self.request, 'download.html', context)
'''



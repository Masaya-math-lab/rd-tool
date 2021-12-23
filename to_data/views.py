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
            # "ThisComputer"
            if request.FILES.get('file'):
                try:
                    df = pd.read_csv(io.StringIO(request.FILES['file'].read().decode(request.POST['encode'])), delimiter=',')
                except UnicodeDecodeError:
                    return render(request, "index.html", {'form': FileUpload, 'message': '※ファイルを読み込めません。他の文字エンコードを選択してください。'})
            # "Web Addressed(URLs)"
            elif request.POST['url']:
                try:
                    df = pd.read_csv(request.POST['url'],encoding=request.POST['encode'])
                except UnicodeDecodeError:
                    return render(request, "index.html", {'form': FileUpload, 'message': '※ファイルを読み込めません。他の文字エンコードを選択してください。'})
            else:
                return render(request, "index.html", {'form': FileUpload, 'message': '※ファイルを選択してください'})

            col = df.columns.values.tolist()
            num = len(col)
            df = df.fillna('')
            df_list = df.to_numpy().tolist()

            # カテゴリーに対応するDATASETを呼び出す
            select_form = SelectColumns()
            select_form.fields['columns'].choices = var.DATASET[request.POST['category']]

            context = {
                'category': request.POST['category'],
                'file': df.to_html(),
                'form': select_form,
                'df': df_list,
                'col': col,
                'num': num,
            }
            return render(request, 'processing.html', context)

        if 'select' in request.POST:
            context = {
                'form': FileName,
                'df': request.POST['df'],
                'col': request.POST['col'],
                'select_col': request.POST.getlist('columns'),
                'category': request.POST['category']
            }
            return render(request, 'download.html', context)

        if 'create' in request.POST:
            form = FileName()
            if request.POST['csv_file']:
                form.fields['csv_file'].initial = request.POST['csv_file']
                file_name = request.POST['csv_file'] + '.csv'
                csv_css = 'block'
                rdf_css = 'none'

            elif request.POST['rdf_file']:
                form.fields['rdf_file'].initial = request.POST['rdf_file']
                file_name = request.POST['rdf_file'] + '.rdf'
                csv_css = 'none'
                rdf_css = 'block'

            context = {
                'file_name': file_name,
                'form': form,
                'df': request.POST['df'],
                'col': request.POST['col'],
                'select_col': request.POST['select_col'],
                'csv_css': csv_css,
                'rdf_css': rdf_css,
                'category': request.POST['category']
            }
            return render(request, 'download.html', context)

        if 'download' in request.POST:
            list = eval(request.POST['df'])
            col = eval(request.POST['col'])
            select_col = eval(request.POST['select_col'])
            df = pd.DataFrame(data=list, columns=col)
            category = request.POST['category']
            file_name = request.POST['file_name']
            response = to_csv(df, category, select_col, file_name)
            return response

    else:
        form = FileUpload
        return render(request, "index.html", {'form': form})



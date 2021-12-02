from django.views import generic
from django.shortcuts import render
from .forms import FileUpload
from .forms import SelectColumns
import csv,io
import pandas as pd

class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = FileUpload

    def form_valid(self, form):
        if 'upload' in self.request.POST:
            df = pd.read_csv(io.StringIO(self.request.FILES['file'].read().decode('utf-8')), delimiter=',')
            col = df.columns.values
            context = {
                'category': form.cleaned_data['category'],
                'col': col,
                'file': df.to_html(),
                'form': SelectColumns()
            }
            return render(self.request, 'processing.html', context)
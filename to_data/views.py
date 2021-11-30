from django.views import generic
from django.shortcuts import render
from .forms import FileUpload
from .forms import SelectColumns

class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = FileUpload

    def form_valid(self, form):
        if 'upload' in self.request.POST:
            context = {
                'category': form.cleaned_data['category'],
                'form': SelectColumns()
            }
            return render(self.request, 'processing.html', context)
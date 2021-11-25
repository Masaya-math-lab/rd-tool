from django.views import generic
from .forms import GetData
# from .forms import ShapingData

class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = GetData

#class ShapingView(generic.FormView):
 #   template_name = 'shaping.html'
  #  form_class = ShapingData
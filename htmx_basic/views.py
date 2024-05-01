from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from htmx_basic.forms import ProductCreateForm


class IndexView(TemplateView):
    template_name = 'htmx_basic/index.html'


class ProductCreateView(FormView):
    form_class = ProductCreateForm
    template_name = 'htmx_basic/product_edit.html'
    success_url = reverse_lazy('htmx_basic:index')

    def form_valid(self, form):
        form.save()  # save the product
        return super().form_valid(form)


def get_name_length(request):
    name = request.POST.get('name')
    length = str(len(name)) if len(name) > 0 else ''
    return HttpResponse(length)

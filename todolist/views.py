from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import (
    ListView
)
from django_htmx.http import trigger_client_event

from htmx_ext import status
from htmx_ext.views import HXCreateView, HXUpdateView, HXDetailView, \
    HXDeleteView
from .forms import TodoForm
from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = 'todolist/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.all().order_by('-due_date', '-created_at')


# Modal Views
class TodoCreateModalView(HXCreateView):
    trigger = 'todoUpdated'
    title = 'Criar novo todo'
    success_message = 'Todo criado com sucesso!'
    model = Todo
    form_class = TodoForm
    template_name = 'todolist/partials/todo_form_modal.html'


class TodoUpdateModalView(HXUpdateView):
    trigger = 'todoUpdated'
    success_message = 'Todo atualizado com sucesso!'
    model = Todo
    form_class = TodoForm
    template_name = 'todolist/partials/todo_form_modal.html'

    def get_title(self):
        return f'Editar {self.object.title}'

class TodoDetailModalView(HXDetailView):
    model = Todo
    template_name = 'todolist/partials/todo_detail_modal.html'
    context_object_name = 'todo'

    def get_title(self):
        return f'Detalhes: {self.object.title}'

class TodoDeleteView(HXDeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        response = HttpResponse('', status=status.HTTP_282_MODAL_DELETE)

        if self.trigger:
            trigger_client_event(response, self.trigger, {})

        if self.success_message:
            messages.success(self.request, self.success_message)
        return response

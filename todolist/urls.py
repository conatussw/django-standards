from django.urls import path
from .views import (
    TodoListView,
    TodoDeleteView,
    TodoCreateModalView,
    TodoUpdateModalView,
    TodoDetailModalView,
)

app_name = 'todolist'

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('novo/modal/', TodoCreateModalView.as_view(), name='todo_create_modal'),
    path('<int:pk>/modal/', TodoDetailModalView.as_view(), name='todo_detail_modal'),
    path('<int:pk>/editar/modal/', TodoUpdateModalView.as_view(), name='todo_update_modal'),
    path('<int:pk>/excluir/', TodoDeleteView.as_view(), name='todo_delete'),
]

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField('Título', max_length=100, blank=False)
    description = models.TextField('Descrição', max_length=255, blank=True)
    due_date = models.DateField('Data do Todo', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    completed = models.BooleanField('Concluído', default=False)

    class Meta:
        ordering = ['-due_date', '-created_at']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todolist:todo_detail', kwargs={'pk': self.pk})

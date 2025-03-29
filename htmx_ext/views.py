from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django_htmx.http import trigger_client_event

from htmx_ext import status


class ModalSingleObjectMixin:
    success_message = None
    trigger = None
    title = None

    def get_title(self):
        """
        Returns the title of the object to be rendered on templates.

        :return: The title of the object.
        :rtype: str
        """
        return self.title

    def get_response(self, instance=None):
        """
        Returns an overridable HttpResponse object with a status code set.

        If the trigger attribute is set, the method will also trigger the client
        event specified by the trigger attribute.

        :param instance: The instance of the object being saved.
        :type instance: The type of the object being saved.
        :return: An HttpResponse object with a status code set.
        :rtype: HttpResponse
        """
        return None

class ModalEditMixin(ModalSingleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context

    def form_valid(self, form):
        instance = form.save()
        return self.get_response(instance)

    def get_response(self,  instance=None):
        return HttpResponse(status=status.HTTP_281_MODAL_CREATE)


class HXCreateView(ModalEditMixin, CreateView):
    def get_response(self,  instance=None):
        response = HttpResponse(status=status.HTTP_281_MODAL_CREATE)

        if self.trigger:
            trigger_client_event(response, self.trigger, {})

        if self.success_message:
            messages.success(self.request, self.success_message)
        return response


class HXUpdateView(ModalEditMixin, UpdateView):
    def get_response(self,  instance=None):
        response = HttpResponse(status=status.HTTP_280_MODAL_UPDATE)

        if self.trigger:
            trigger_client_event(response, self.trigger, {})

        if self.success_message:
            messages.success(self.request, self.success_message)
        return response

class HXDetailView(ModalEditMixin, DetailView):
    pass

class HXDeleteView(ModalSingleObjectMixin, DeleteView):
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return self.get_response()

    def get_response(self,  instance=None):
        response = HttpResponse(status=status.HTTP_282_MODAL_DELETE)

        if self.trigger:
            trigger_client_event(response, self.trigger, {})

        if self.success_message:
            messages.success(self.request, self.success_message)

        return response

from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def hx_dialog_js():
    """
    Insere o script HTMX para diálogos modais.
    Uso: {% load htmx_ext %} ... {% hx_dialog_js %}
    """
    script_url = static('htmx_ext/dialogs.js')
    return mark_safe(f'<script src="{script_url}"></script>')

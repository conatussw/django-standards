from django.urls import path

from . import views

app_name = 'htmx_basic'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('get-length/', views.get_name_length, name='get_name_length'),

]

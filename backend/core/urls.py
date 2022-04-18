from django.urls import path

from .views import index, run_task

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('task/print-numbers/', run_task, name='run_task'),
]

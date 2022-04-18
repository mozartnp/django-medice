from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .tasks import print_numbers


def index(request):
    return render(request, 'core/index.html')


def run_task(request):
    print_numbers.delay(5)
    url = 'core:index'
    return HttpResponseRedirect(reverse(url))

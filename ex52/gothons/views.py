from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse


def start(request):
    return render(request, 'gothons/index.html', {'msg': 'index'})

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

greeting = "Hello World"


def home(request):
    page_title = 'Gothons From Planet Percal #25'
    greeting = "Hello World"

    if request.GET != {}:
        greeting = request.GET['greeting']

    context = {'greeting': greeting, 'page_title': page_title}
    return render(request, 'index.html', context)


def change(request):
    page_title = 'Sample Web Form'
    context = {'page_title': page_title}
    return render(request, 'hello_form.html', context)


def form_handle(request):
    greeting = "Something went wrong"

    if request.method == "POST":
        greeting = "%s %s" % (request.POST['greeting'], request.POST['name'])

    # passing as get, should use something else or handle differently in real world
    return HttpResponseRedirect(reverse('home') + '?greeting=%s' % greeting)

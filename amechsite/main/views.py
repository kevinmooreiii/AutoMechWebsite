from django.shortcuts import render
from django.template import loader


def index(request):
    """ Homepage
    """
    # index_template = loader.get_template('main/index.html')
    # return HttpResponse(template.render(index_template, request))
    return render(request, 'index.html')


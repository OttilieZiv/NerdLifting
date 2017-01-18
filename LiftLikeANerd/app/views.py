"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from extra_views.advanced import CreateWithInlinesView, UpdateWithInlinesView
from . import models

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def search_exercises(request):
    return render(request, 'search_exercises.html')
    
class ProgrammeList(ListView):
    model = models.Programme
    template_name = 'programme_list.html'
    context_object_name = 'prog_list'
    
class ProgrammeUpdate(UpdateView):
    model = models.Programme
    fields = ['name', 'date_started']
    
    def get_success_url(self):
        return reverse('prog_list', kwargs={'pk':self.kwargs.get('pk',None)})
    
class ProgrammeCreate(CreateView):
    model = models.Programme
    fields = ['name', 'date_started']
    
    def get_success_url(self):
        return reverse('prog_list', kwargs={'pk':self.kwargs.get('pk',None)})

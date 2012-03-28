from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

import json

from . import forms 


def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = forms.DeviceAssignForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = forms.DeviceAssignForm() # An unbound form
    setup = json.load(open('setup.json'))
    return render_to_response('index.html', {'setup': setup, 'form': form}, 
            context_instance=RequestContext(request))

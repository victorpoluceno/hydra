from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

import json

from . import forms
from . import models

from socketio import socketio_manage
from socketio.namespace import BaseNamespace


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
    return render_to_response('index.html', {'socketio': request.META['HTTP_HOST'], 'form': form}, 
            context_instance=RequestContext(request))
    

def socketio(request):
    class PlayNameSpace(BaseNamespace):
        def recv_connect(self):
            print 'horray, connect'

        def recv_initialize(self):
            print 'horray, recv_initialize'

        def on_guid(self, val):
            print val
            print models.Campaign.objects.all()
            self.emit('load', 'sdsdsdsdsds')
            
    socketio_manage(request.environ, {'': PlayNameSpace})
    return HttpResponse()

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core import serializers


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
    return render_to_response('index.html', {'socketio': request.META['HTTP_HOST'],
            'form': form}, context_instance=RequestContext(request))
    

def socketio(request):
    class PlayNameSpace(BaseNamespace):
        def recv_connect(self):
            print 'horray, connect'

        def recv_initialize(self):
            print 'horray, recv_initialize'

        def on_guid(self, val):
            print val
            
            data = []
            campaign_list = models.Schedule.objects.filter(device__guid=val)
            if campaign_list:
                for r in campaign_list:                    
                    data.append({'movie': r.campaign.movie.url, 
                        'start_time': r.start_time.isoformat(), 
                        'end_time': r.end_time.isoformat()})

            print data
            self.emit('load', data)
            
    socketio_manage(request.environ, {'': PlayNameSpace})
    return HttpResponse()

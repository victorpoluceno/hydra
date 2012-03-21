from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

import json


def index(request):
    setup = json.load(open('setup.json'))
    return render_to_response('index.html', setup, 
            context_instance=RequestContext(request))
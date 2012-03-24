from django.db import models
from django.forms import ModelForm

from . import models


class DeviceAssignForm(ModelForm):
    class Meta:
        model = models.Device

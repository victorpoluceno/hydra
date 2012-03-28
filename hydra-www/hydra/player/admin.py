from django.contrib import admin

from . models import Campaign, Schedule ,Device


admin.site.register(Schedule)
admin.site.register(Campaign)
admin.site.register(Device)

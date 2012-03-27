from django.contrib import admin

from player.models import Campaign, Schedule ,Device

#TODO add other columns main list view


class ScheduleInline(admin.TabularInline):
    model = Schedule



class CampaignAdmin(admin.ModelAdmin):
    inlines = [
        #ScheduleInline,
    ]


class DeviceAdmin(admin.ModelAdmin):
    inlines = [
        #ScheduleInline,
    ]


admin.site.register(Schedule)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Device, DeviceAdmin)
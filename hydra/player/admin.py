from django.contrib import admin

from player.models import Campaing, PlayList, Movie, Device

admin.site.register(Campaing)
admin.site.register(PlayList)
admin.site.register(Movie)
admin.site.register(Device)
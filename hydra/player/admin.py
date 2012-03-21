from django.contrib import admin

from player.models import PlayList, PlayListMovie, Movie, Device


class PlayListMovieInline(admin.TabularInline):
    model = PlayListMovie


class PlayListAdmin(admin.ModelAdmin):
    inlines = [
        PlayListMovieInline,
    ]


admin.site.register(PlayList, PlayListAdmin)
admin.site.register(Movie)
admin.site.register(Device)
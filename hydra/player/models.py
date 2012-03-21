from django.db import models

from player.validators import FileValidator


class Campaing(models.Model):
    title = models.CharField(max_length=250)
    playlist = models.ForeignKey('player.PlayList')

    def __unicode__(self):
        return self.title


class PlayList(models.Model):
    title = models.CharField(max_length=250)
    movies = models.ManyToManyField('player.Movie')

    def __unicode__(self):
        return self.title


class Movie(models.Model):
    original_file = models.FileField(upload_to="movies/",
        validators=[FileValidator(max_size=25 * 1204 * 1024,
        allowed_mimetypes=('video/mp4', 'video/webm'),
        allowed_extensions=('mp4', 'webm'))])

    def __unicode__(self):
        return self.original_file.name


class Device(models.Model):
    title = models.CharField(max_length=250)
    guid = models.IntegerField(editable=False)

    def __unicode__(self):
        return self.title

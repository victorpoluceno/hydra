from django.db import models

from player.validators import FileValidator


class PlayList(models.Model):
    title = models.CharField(max_length=250)
    movies = models.ManyToManyField('player.Movie',
        through='player.PlayListMovie')

    def __unicode__(self):
        return self.title


class Movie(models.Model):
    original_file = models.FileField(upload_to='movies/',
        validators=[FileValidator(max_size=25 * 1204 * 1024,
        allowed_mimetypes=('video/mp4', 'video/webm'),
        allowed_extensions=('mp4', 'webm'))])

    def __unicode__(self):
        return self.original_file.name


class PlayListMovie(models.Model):
    movie = models.ForeignKey(Movie)
    playlist = models.ForeignKey(PlayList)
    order = models.IntegerField(unique=True)
    

class Device(models.Model):
    title = models.CharField(max_length=250)
    guid = models.IntegerField()
    playlist = models.ForeignKey('player.PlayList', blank=True, null=True)

    def __unicode__(self):
        return self.title

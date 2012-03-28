from django.db import models

from . import validators


class Campaign(models.Model):
    title = models.CharField(max_length=250)
    devices = models.ManyToManyField('player.Device',
        through='player.Schedule')
    movie = models.FileField(upload_to='movies/',
        validators=[validators.FileValidator(max_size=25 * 1204 * 1024,
        allowed_mimetypes=('video/mp4', 'video/webm'),
        allowed_extensions=('mp4', 'webm'))])

    def __unicode__(self):
        return self.title


class Schedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    device = models.ForeignKey('player.Device')
    campaign = models.ForeignKey('player.Campaign') 


class Device(models.Model):
    title = models.CharField(max_length=250)
    guid = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

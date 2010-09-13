from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from managers import URLManager
from django.db import models

class URL(models.Model):
    """ A URL that exists in order to alias an object to a different location. """

    class Meta(object):
        verbose_name = 'URL'

    location = models.CharField(max_length=128)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    related_object = generic.GenericForeignKey()

    # Custom manager for getting related items easily
    objects = URLManager()

    def get_related_url(self):
        if hasattr(self.related_object, 'get_absolute_url'):
            return self.related_object.get_absolute_url()

    def get_absolute_url(self):
        return self.location

    def __unicode__(self):
        return self.location


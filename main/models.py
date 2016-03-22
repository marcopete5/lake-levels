from __future__ import unicode_literals

from django.db import models
from .slug import unique_slugify

# Create your models here.

class Lake(models.Model):
	name = models.CharField(max_length=30)
	url = models.URLField()
	latitude = models.FloatField(null=True, blank=True, editable=False)
	longitude = models.FloatField(null=True, blank=True, editable=False)
	slug = models.SlugField(max_length=255, unique=True, help_text='A label for URL config.')

	def __str__(self):
		return self.name

	def save(self, **kwargs):
		slug = '%s' % (self.name)
		unique_slugify(self, slug)
		super(Lake, self).save()

		
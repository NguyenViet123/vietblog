from django.db import models
from django.utils import timezone
# Create your models here.

from django.db.models import TextField


class NonStrippingTextField(TextField):
    """A TextField that does not strip whitespace at the beginning/end of
    it's value.  Might be important for markup/code."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingTextField, self).formfield(**kwargs)

class About(models.Model):
	title = models.CharField(max_length=200)
	text = NonStrippingTextField()
	created_data = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	# def __init__(self, *args, **kwargs):
	# 	self.text.strip = False



class Post(models.Model):
	author= models.CharField(max_length=40)
	title = models.CharField(max_length=200)
	text = NonStrippingTextField()
	created_data = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	# def __init__(self, *args, **kwargs):
	# 	self.text.strip = False


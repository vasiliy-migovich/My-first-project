# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

class Visit(models.Model):

	class Meta(object):
		verbose_name = u"Відвідування"
		verbose_name_plural = u"Відвідування"

	def __unicode__(self):
		return u"%s %s" % (self.last_name, self.first_name)


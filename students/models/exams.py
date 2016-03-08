# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

class Exam(models.Model):

	class Meta(object):
		verbose_name = u"Іспит"
		verbose_name_plural = u"Іспити"

	""" Exams model """
	title_exam = models.CharField(
	    max_length=45,
	    blank=False,
	    verbose_name=u"Назва предмету")

	date_exam = models.DateTimeField(
	    blank=False,
	    verbose_name=u"Дата і час екзамену",
	    null=True)

	examiner = models.CharField(
		blank=False,
		null=True,
        max_length=255,
        verbose_name=u"Викладач")

	group_exam = models.ForeignKey('Group',
		blank=False,
		null=True,
        max_length=45,
        verbose_name=u"Вибрати групу")

	def __unicode__(self):
		return u"%s (%s, %s, %s)" % (self.title_exam, self.date_exam, self.examiner, self.group_exam)


# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.exams import Exam

# Views for Exams
def exams_list(request):
	exams = Exam.objects.all()

	order_by = request.GET.get('order_by', '')
	if order_by in ('title_exam', 'date_exam', 'examiner', 'group_exam'):
		exams = exams.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exams = exams.reverse()

	# paginate exams
	paginator = Paginator(exams, 5)
	page = request.GET.get('page')
	try:
		exams = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		exams = paginator.page(1)
	except EmptyPage:	
		# If page is out of range (e.g. 9999), deliver
		# last page of results.
		exams = paginator.page(paginator.num_pages)

	return render(request, 'students/exams_list.html', 
		{'exams': exams})
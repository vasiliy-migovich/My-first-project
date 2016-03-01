# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import calendar

from ..models.exams import Exam
from ..models.students import Student

# Views for Students
def exams_list(request):
	students = Student.objects.all()

	exams = Exam.objects.all()
	value = [2, 3, 4, 5]

	# try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	# paginate students
	paginator = Paginator(students, 5)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		students = paginator.page(1)
	except EmptyPage:	
		# If page is out of range (e.g. 9999), deliver
		# last page of results.
		students = paginator.page(paginator.num_pages)

	return render(request, 'students/exams_list.html', 
		{'students': students, 'exams': exams, 'value': value})
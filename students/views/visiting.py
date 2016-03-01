# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import calendar

from ..models.visiting import Visit
from ..models.students import Student

# Views for Students
def visiting_list(request):
	students = Student.objects.all()
	
	#list_months = {1:u'Січень', 2:'Лютий', 3:'Березень', 4:'Квітень', 5:'Травень', 6:'Червень', 7:'Липень', 8:'Серпень', 9:'Вересень', 10:'Жовтень' , 11:'Листопад', 12:'Грудень'}

	# try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	# paginate students
	paginator = Paginator(students, 3)
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

	return render(request, 'students/visiting_list.html', 
		{'students': students})
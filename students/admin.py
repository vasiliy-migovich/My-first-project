from django.contrib import admin
from .models.students import Student
from .models.groups import Group
from .models.visiting import Visit
from .models.exams import Exam

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Visit)
admin.site.register(Exam)

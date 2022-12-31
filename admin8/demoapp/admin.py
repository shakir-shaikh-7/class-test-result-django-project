from django.contrib import admin
from demoapp.models import Student,Mobilephone,Subcriber

# Register your models here.

admin.site.register(Student)      
admin.site.register(Subcriber)      
admin.site.register(Mobilephone)
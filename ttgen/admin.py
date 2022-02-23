from django.contrib import admin
from.models import *
from .views import timetable
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from import_export.admin import ImportExportModelAdmin
from django.contrib.sites.models import Site
from django_object_actions import DjangoObjectActions

# class ImportAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/generate_table.html'


admin.site.site_header = 'سیستم طراحی جدول زمان بندی کلاس ها'
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.unregister(Site)

class RoomAdmin(ImportExportModelAdmin):
	pass    
class InstructureAdmin(ImportExportModelAdmin):
	pass    
class MeetingTimeAdmin(ImportExportModelAdmin):
	pass    
class CourseAdmin(ImportExportModelAdmin):
	pass    
class DepartmentAdmin(ImportExportModelAdmin):
	pass    
class SectionAdmin(ImportExportModelAdmin):
	pass    


admin.site.register(Room, RoomAdmin)
admin.site.register(Instructor, InstructureAdmin)
admin.site.register(MeetingTime, MeetingTimeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Section, SectionAdmin)

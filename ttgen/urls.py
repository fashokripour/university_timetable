from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin

admin.site.index_title = 'ورود اطلاعات'                 # default: "Site administration"

class AccessUser:
    has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True

admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True
from django.contrib.admin.models import LogEntry

# LogEntry.objects.all().delete()

urlpatterns = [
    path('',  index, name='index'),
    path('about',  about, name='about'),
    path('help',  help, name='help'),
    path('terms',  terms, name='terms'),
    path('contact',  contact, name='contact'),
    path('import_data',  import_data, name = 'import_data'),

    path('timetable_generation/',  timetable, name='timetable'),
    # path('timetimetable_generation/doanload', Pdf, name='download')
    # path('timetable_generation/render/pdf',  Pdf, name='pdf'),

]

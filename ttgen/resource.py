from pyexpat import model
from import_export import recources
from .models import *
from import_export import fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget

class RoomResource(recources.ModelResource):
    class Meta:
        model = Room

class InstructorResource(recources.ModelResource):
    class Meta:
        model = Instructor

class MeetingTimeResource(recources.ModelResource):
    class Meta:
        model = MeetingTime

class CourseRecourse(recources.ModelResource):
    instructors = fields.Field(column_name='instructors', attribute='instructors', widget=ManyToManyWidget(model=Instructor,field='name'))
    class Meta:
        model = Course

class DepartmentRecourse(recources.ModelRecourse):
    courses = fields.Field(column_name='courses', attribute='courses', widget=ManyToManyWidget(model=Course,field='name'))
    class Meta:
        model = Department

class SectionRecourse(recources.ModelRecourse):
    department = fields.Field(colmun_name = 'department', attribute = 'department', widget= ForeignKeyWidget(model = Department, field = 'name'))
    course = fields.Field (colmun_name = 'course', attribute = 'course', widget= ForeignKeyWidget(model = Course ,field = 'name'))
    meeting_time = fields.Field(colmun_name = 'meeting_time', attribute = 'meeting_time', widget= ForeignKeyWidget(model = MeetingTime, field = 'name'))
    room = fields.Field(colmun_name = 'room', attribute = 'room', widget= ForeignKeyWidget(model = Room, field = 'name'))
    instructor = fields.Field(colmun_name = 'instructor', attribute = 'instructor', widget= ForeignKeyWidget(model = Instructor, field = 'name'))
    class Meta:
        model = Section
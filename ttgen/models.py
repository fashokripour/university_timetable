from django.db import models


POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1

class Room(models.Model):
    id = models.IntegerField(unique=True, primary_key=True , verbose_name='شناسه')
    seating_capacity = models.IntegerField( verbose_name='ظرفیت کلاس')

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = 'کلاس ها'


class Instructor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, verbose_name = 'شناسه')
    name = models.CharField(max_length=25, verbose_name = 'نام')

    def __str__(self):
        return f'{self.id} {self.name}'
    class Meta:
        verbose_name_plural = 'اساتید'


class MeetingTime(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name = 'شناسه')
    time = models.CharField(max_length=50, verbose_name = 'ساعت')
    day = models.CharField(max_length=15, verbose_name = 'زمان')
    # time = models.CharField(max_length=50, choices=time_slots, default='11:30 - 12:30')
    # day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f'{self.id} {self.day} {self.time}'
    class Meta:
        verbose_name_plural = 'ساعت ها'

    

class Course(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name = 'شناسه')
    course_name = models.CharField(max_length=40, verbose_name = 'نام')
    max_numb_students = models.CharField(max_length=100,verbose_name = 'ظرفیت دانشجو')
    instructors = models.ManyToManyField(Instructor, verbose_name = 'نام مدرسان')

    def __str__(self):
        return f'{self.id} {self.course_name}'
    class Meta:
        verbose_name_plural = 'واحد های درسی'



class Department(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, verbose_name = 'شناسه')
    dept_name = models.CharField(max_length=50, verbose_name = 'نام دانشکده')
    courses = models.ManyToManyField(Course, verbose_name = 'دروس دانشکده')

    def get_courses(self):
        return self.courses

    def __str__(self):
        return self.dept_name
    class Meta:
        verbose_name_plural = 'دانشکده'



class Section(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, verbose_name = 'شناسه')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name = 'نام دانشکده')
    num_class_in_week = models.IntegerField(verbose_name = 'تعداد کلاس در هفته')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'نام درس')
    meeting_time = models.ForeignKey(MeetingTime, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'ساعت درس')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'کلاس')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'استاد')

    def set_room(self, room):
        section = Section.objects.get(pk = self.id)
        section.room = room
        section.save()

    def set_meetingTime(self, meetingTime):
        section = Section.objects.get(pk = self.id)
        section.meeting_time = meetingTime
        section.save()

    def set_instructor(self, instructor):
        section = Section.objects.get(pk=self.id)
        section.instructor = instructor
        section.save()
    class Meta:
        verbose_name_plural = 'گروه های درسی'
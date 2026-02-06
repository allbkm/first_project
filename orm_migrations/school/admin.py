from django.contrib import admin
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'display_teachers')
    list_filter = ('teachers',)
    search_fields = ('name',)
    filter_horizontal = ('teachers',)

    def display_teachers(self, obj):
        teachers_list = [teacher.name for teacher in obj.teachers.all()]
        if teachers_list:
            return ", ".join(teachers_list)
        return "Нет учителей"
    display_teachers.short_description = 'Учителя'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'student_count')
    search_fields = ('name', 'subject')

    def student_count(self, obj):
        return obj.students.count()
    student_count.short_description = 'Количество учеников'

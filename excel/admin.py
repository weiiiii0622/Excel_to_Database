from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

from .models import Info, User, Lesson


@admin.register(Info)
class InfoAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'gender', 'school', 'grade', 'lesson')
    list_filter = ('name', 'gender', 'school', 'grade', 'lesson')

    fieldsets = (
        (None, {'fields': ('name', 'gender', 'school', 'grade', 'lesson')}),
        #('Event info', {'fields': ('date', 'test', 'scope', 'grade',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'gender', 'school', 'grade', 'lesson'),
        }),
    )
    
    search_fields = ('name', 'gender', 'school', 'grade', 'lesson')
    ordering = ('name', 'lesson')
    filter_horizontal = ()

@admin.register(User)
class UserAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'gender', 'school', 'grade', 'lesson_selected', 'lesson_count')
    list_filter = ('name', 'gender', 'school', 'grade', 'lesson_count')

    fieldsets = (
        (None, {'fields': ('name', 'gender', 'school', 'grade',)}),
        ('Event info', {'fields': ('lesson_selected', 'lesson_count',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'gender', 'school', 'grade', 'lesson_selected', 'lesson_count'),
        }),
    )
    
    search_fields = ('name', 'gender', 'school', 'grade', 'lesson_selected', 'lesson_count',)
    ordering = ('name', 'lesson_count')
    filter_horizontal = ()

@admin.register(Lesson)
class LessonAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'limit', 'total', 'start', 'end',)
    list_filter = ('name', 'limit', 'total', 'start', 'end',)

    fieldsets = (
        (None, {'fields': ('name', 'limit', 'total', 'start', 'end',)}),
        #('Event info', {'fields': ('class_selected', 'class_count',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'limit', 'total', 'start', 'end'),
        }),
    )
    
    search_fields = ('name', 'limit', 'total', 'start', 'end',)
    ordering = ('name', 'total')
    filter_horizontal = ()

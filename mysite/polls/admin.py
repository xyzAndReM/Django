
from django.contrib import admin

from .models import List, Choice, Question


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class ListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['list_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        (None,               {'fields': ['question_text2']}),
        (None,               {'fields': ['question_text3']}),
        (None,               {'fields': ['image']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(List, ListAdmin)
admin.site.register(Question,QuestionAdmin)
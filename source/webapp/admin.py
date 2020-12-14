from django.contrib import admin

from webapp.forms import AnswerInlineFormSet
from webapp.models import Test, Question, Answer, Choice


class AnswerInline(admin.StackedInline):

    model = Answer
    formset = AnswerInlineFormSet
    min_num = 2
    extra = 0


class QuestionAdmin(admin.ModelAdmin):

    inlines = [AnswerInline]


class TestInstanceInline(admin.TabularInline):
    model = Question


class TestAdmin(admin.ModelAdmin):
    inlines = [TestInstanceInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

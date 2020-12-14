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


admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

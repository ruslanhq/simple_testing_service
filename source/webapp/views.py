from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from webapp.models import Test, Question, Answer, Choice


class TestView(ListView):
    template_name = 'index.html'
    context_object_name = 'tests'
    model = Test
    ordering = '-created_at'
    paginate_by = 5


class TestDetail(DetailView):
    template_name = 'questions.html'
    context_object_name = 'test'
    model = Test


class ChoiceView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        question = self.get_object()
        test_pk = kwargs.get('test_id')
        if question:
            return render(request, 'choice.html', {'question': question})
        return redirect('result', test_pk)

    def get_object(self):
        test_pk = self.kwargs.get('test_id')
        question = Question.objects.filter(test_id=test_pk, choices__user__isnull=True)
        if not len(question) == 0:
            return get_object_or_404(question, pk=question.first().pk)

    def post(self, request, *args, **kwargs):
        test_id = kwargs.get('test_id')
        answer_id = request.POST.get('answer')
        user = self.request.user
        answer = get_object_or_404(Answer, pk=answer_id)
        question = Question.objects.filter(test_id=test_id, choices__user__isnull=True).first()
        Choice.objects.create(question=question, choice=answer, user=user, is_completed=True)
        return redirect('pass_choice', test_id)


class ResultView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        test = get_object_or_404(Test, pk=kwargs.get('pk'))
        user = self.request.user
        choice_valid = Choice.objects.filter(user=user, question__test=test, choice__is_valid=True).distinct()
        choice_in_valid = Choice.objects.filter(user=user, question__test=test, choice__is_valid=False).distinct()
        percent = round(len(choice_valid) / test.questions.count() * 100, 2)
        return render(request, 'result.html', context={'test': test, 'choice_v': len(choice_valid),
                                                       'choice_i': len(choice_in_valid), 'percent': percent})


class ResetResultView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        test = get_object_or_404(Test, pk=kwargs.get('pk'))
        user = self.request.user
        choices = Choice.objects.filter(user=user, question__test=test)

        for choice in choices:
            choice.delete()
        return redirect('pass_choice', test.pk)

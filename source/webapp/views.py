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


class ChoiceView(View):
    def get(self, request, *args, **kwargs):
        question = self.get_object()
        if question:
            return render(request, 'choice.html', {'question': question})
        return redirect('index')

    def get_object(self):
        test_pk = self.kwargs.get('test_id')
        question = Question.objects.filter(test_id=test_pk, is_completed=False)
        if not len(question) == 0:
            return get_object_or_404(question, pk=question.first().pk)

    def post(self, request, *args, **kwargs):
        test_id = kwargs.get('test_id')
        answer_id = request.POST.get('answer')
        question = Question.objects.filter(test_id=test_id, is_completed=False).first()
        answer = get_object_or_404(Answer, pk=answer_id)
        Choice.objects.create(question=question, choice=answer)
        question.is_completed = True
        question.save()
        return redirect('pass_choice', test_id)

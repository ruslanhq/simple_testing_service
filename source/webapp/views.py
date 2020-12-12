from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Test, Question


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


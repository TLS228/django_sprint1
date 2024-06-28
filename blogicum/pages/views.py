from django.shortcuts import render
from django.http import HttpResponse


def about(request) -> HttpResponse:
    """Описание проекта."""
    template: str = 'pages/about.html'
    return render(request, template)


def rules(request) -> HttpResponse:
    """Правила проекта."""
    template: str = 'pages/rules.html'
    return render(request, template)

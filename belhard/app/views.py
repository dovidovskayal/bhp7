from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET
from .models import Category
from django.shortcuts import render, get_object_or_404


def index(request: HttpRequest):
    categories = Category.objects.all().order_by('name')
    return render(request, 'app/index.html', {'categories': categories}, status=200)


def error404(request, exception):
    return HttpResponse('<b>404</b>')
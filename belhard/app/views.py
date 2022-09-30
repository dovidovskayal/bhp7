from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET
from .models import Category
from django.shortcuts import render, get_object_or_404


@require_GET
def index(request: HttpRequest, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    # if not category:
    #     raise Http404
    return HttpResponse('<b>HELLO</b>')


def error404(request, exception):
    return HttpResponse('<b>404</b>')
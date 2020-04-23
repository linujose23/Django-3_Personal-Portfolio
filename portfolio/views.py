from django.shortcuts import render
from .models import portfolio_model
# Create your views here.


def index(request):

    text = {'text': 'this is a Portfolio Page!'}

    objects = portfolio_model.objects.all()

    return render(request, 'portfolio/home.html', {'all_apps': objects})

#fly/views.py
from django.views.generic import ListView
from .models import Todo

class HomePageView(ListView):
    model = Todo
    template_name = "fly/home.html"


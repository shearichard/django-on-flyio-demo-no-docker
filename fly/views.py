#fly/views.py
from django.views.generic import ListView
from .models import Todo

class HomePageView(ListView):
    model = Todo
    template_name = "fly/home.html"
    context_object_name = 'todo_list'
    ordering = ['todo']


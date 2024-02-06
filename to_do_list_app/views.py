from django.shortcuts import render
from .models import ToDoItems
from django.views.generic import (
    ListView,
    DetailView,
)
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


class ToDoListView(ListView):
    model = ToDoItems
    template_name = "home.html"


class ToDoDescriptionView(DetailView):
    model = ToDoItems
    template_name = "description.html"


class ToDoCreateView(CreateView):
    # todo_items = ToDoItems.objects.all()
    model = ToDoItems
    template_name = "new.html"
    fields = [
        "title",
        "description",
        "due_date",
        "completion_status",
    ]


class ToDoUpdateView(UpdateView):
    model = ToDoItems
    template_name = "update.html"
    fields = ["title", "description", "due_date", "completion_status"]


class ToDoDeleteView(DeleteView):
    model = ToDoItems
    template_name = "delete.html"
    success_url = reverse_lazy("home")


# Create your views here.

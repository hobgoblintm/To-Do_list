from django.urls import path
from .views import (
    ToDoListView,
    ToDoDescriptionView,
    ToDoCreateView,
    ToDoUpdateView,
    ToDoDeleteView,
)


urlpatterns = [
    path("todo/<int:pk>/delete/", ToDoDeleteView.as_view(), name="delete"),
    path("todo/<int:pk>/edit/", ToDoUpdateView.as_view(), name="edit"),
    path("todo/new/", ToDoCreateView.as_view(), name="new"),
    path("", ToDoListView.as_view(), name="home"),
    path("todo/<int:pk>/", ToDoDescriptionView.as_view(), name="description"),
]

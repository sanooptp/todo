from django.urls import include, path
from . import views


urlpatterns = [
    path("list/", views.TodoListView.as_view(), name='list'),
    path("listitems/", views.TodoListByoneView.as_view(), name='list'),
    path("create/", views.TodoCreateView.as_view(), name='create'),
    path("update/<int:pk>/", views.TodoUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", views.TodoDeleteView.as_view(), name='delete'),
]

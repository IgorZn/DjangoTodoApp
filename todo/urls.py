from django.urls import path
from todo.views import (
    TaskList,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('<int:pk>', TaskDetailView.as_view(), name='task'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('add', TaskCreateView.as_view(), name='task-create'),
]
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

"""
    Use the LoginRequiredMixin class to protect a page.
"""

def home(request):
    return render(request, 'home.html')


class TaskList(LoginRequiredMixin, ListView):
    """
        - model указывает объекты, из модели которых вы хотите отобразить.
        В этом примере мы используем модель Task. Внутри Django запросит
        все объекты из модели Task (Task.objects.all()) и передаст их в шаблон.

        - context_object_name указывает имя переменной списка моделей в шаблоне.
        По умолчанию Django использует object_list. Однако имя object_list довольно
        общее. Поэтому мы переопределяем context_object_name, устанавливая его
        значение для задач.
    """
    model = Task
    context_object_name = 'tasks'
    """
        - В данном случае изменив 'context_object_name' на 'tasks' в
        шаблоне мы обращаемся не к 'object_list', а к 'tasks'
        
        # task_list.html
        ...
            {% for task in tasks %}
                <li><a href="#" class="{% if task.completed %}completed{% endif %}">{{ task.title }}</a>
                    <div class="task-controls">
                        <a href="#"><i class="bi bi-trash"></i> </a>
                        <a href="#"><i class="bi bi-pencil-square"></i></a>
                    </div>
                </li>
            {% endfor %}
        ...
    """
    template_name = 'app/task_list.html'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'app/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    - model указывает класс создаваемого объекта (Задача).

    - fields — это список полей, которые отображаются в форме.
    В этом примере форма будет отображать заголовок, описание
    и завершенные атрибуты модели задачи.

    - Success_url — это целевой URL-адрес, на который Django
    перенаправит после успешного создания задачи. В этом примере
    мы перенаправляемся на список задач с помощью функции reverse_lazy().
    Функция reverse_lazy() принимает имя представления и возвращает
    URL-адрес.

    - form_valid() — метод, вызываемый после успешной публикации формы.
    В этом примере мы устанавливаем пользователя как текущего вошедшего
    в систему пользователя, создаем мгновенное сообщение и возвращаем
    результат метода form_valid() суперкласса.

    """
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    template_name = 'app/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = "app/task_update.html"
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "app/task_delete.html"
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "The task was delete successfully.")
        return super(TaskUpdateView, self).form_valid(form)
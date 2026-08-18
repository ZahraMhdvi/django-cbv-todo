from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)




class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)





class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)




class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-list")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)




class TaskDoneView(LoginRequiredMixin, View):

    def post(self, request, pk):
        task = get_object_or_404(
            Task,
            pk=pk,
            user=request.user,
        )

        task.is_done = True
        task.save(update_fields=["is_done"])

        return redirect("tasks:task-list")
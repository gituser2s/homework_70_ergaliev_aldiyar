from django.shortcuts import redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Task, Project
from webapp.forms import TaskForm, ProjectForm


class ProjectCreateView(CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    template_name = 'project_update.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')


class ProjectConfirmDeleteView(TemplateView):
    template_name = 'project_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Task, pk=kwargs['pk'])
        project.delete()
        return redirect('project_index')


class ProjectDetail(DetailView):
    template_name = 'project.html'
    model = Project


from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView

from issuetracker.forms import IssueForm, StatusForm, SearchForm, ProjectForm
from issuetracker.models import Issue, Status, Project


class IssueListView(ListView):
    template_name = 'index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['-updated_at']
    paginate_by = 10
    paginate_orphans = 5

    search_form = SearchForm
    search_value = None

    def get(self, request, *args, **kwargs):
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_value:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_value) |
                Q(description__icontains=self.search_value) |
                Q(summary__iexact=self.search_value) |
                Q(description__iexact=self.search_value)
            )

        return queryset

    def get_search_value(self):
        search_form = self.search_form(self.request.GET)
        if search_form.is_valid():
            return search_form.cleaned_data['search']


class CreateIssueView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'create_issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        context['project'] = project
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                project_id=kwargs['pk'],
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type'],
            )
            issue.save()
            return HttpResponseRedirect(reverse('issue', args=[issue.id]))

        return render(request, 'create_issue.html', context={'form': form})


class CreateStatusView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'create_status.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('issues'))

        return render(request, self.template_name, {'form': form})


class IssueDetailView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=self.kwargs['pk'])
        return context


class UpdateIssueView(LoginRequiredMixin, UpdateView):
    model = Issue
    template_name = 'update_issue.html'
    context_object_name = 'issue'
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue', args=[self.get_object().pk])


class DeleteIssueView(LoginRequiredMixin, DeleteView):
    model = Issue

    def get_success_url(self):
        return reverse('issues')


class ProjectListView(ListView):
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-start']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = context.get('project').issues.all()
        context['issue_form'] = IssueForm()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create_project.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            project = form.save()
            return HttpResponseRedirect(reverse('project', args=[project.pk]))

        return render(request, self.template_name, {'form': form})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/update_project.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            project = form.save()
            return HttpResponseRedirect(reverse('project', args=[project.pk]))

        return render(request, self.template_name, {'form': form})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('projects')

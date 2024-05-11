from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView

from issuetracker.forms import IssueForm, StatusForm
from issuetracker.models import Issue, Status


class IssueListView(ListView):
    def get(self, request, *args, **kwargs):
        issues = Issue.objects.all()
        context = {'issues': issues}
        return render(request, 'index.html', context)


class CreateIssueView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'create_issue.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            issue = form.save()
            return HttpResponseRedirect(reverse('issue', args=[issue.id]))

        return render(request, 'create_issue.html', {'form': form})


class CreateStatusView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'create_status.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('issues'))

        return render(request, 'create_status.html', {'form': form})


class IssueDetailView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=self.kwargs['pk'])
        return context


class UpdateIssueView(UpdateView):
    model = Issue
    template_name = 'update_issue.html'
    context_object_name = 'issue'
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue', args=[self.get_object().pk])


class DeleteIssueView(DeleteView):
    model = Issue

    def get_success_url(self):
        return reverse('issues')

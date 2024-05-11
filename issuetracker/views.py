from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView

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
            return HttpResponseRedirect(reverse('issues'))

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

        return render(request, 'create_issue.html', {'form': form})

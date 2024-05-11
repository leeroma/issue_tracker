from django.shortcuts import render
from django.views.generic import ListView

from issuetracker.models import Issue


class IssueListView(ListView):
    def get(self, request, *args, **kwargs):
        issues = Issue.objects.all()
        context = {'issues': issues}
        return render(request, 'index.html', context)

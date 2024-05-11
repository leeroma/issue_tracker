from django.urls import path

from issuetracker.views import IssueListView

urlpatterns = [
    path('', IssueListView.as_view(), name='issues'),
]

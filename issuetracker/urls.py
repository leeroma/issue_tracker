from django.urls import path

from issuetracker.views import IssueListView, CreateIssueView, CreateStatusView, IssueDetailView

urlpatterns = [
    path('', IssueListView.as_view(), name='issues'),
    path('create_issue', CreateIssueView.as_view(), name='create_issue'),
    path('create_status', CreateStatusView.as_view(), name='create_status'),
    path('issue/<int:pk>', IssueDetailView.as_view(), name='issue'),

]

from django.urls import path

from issuetracker.views import IssueListView, CreateIssueView, CreateStatusView, IssueDetailView, UpdateIssueView, \
    DeleteIssueView

urlpatterns = [
    path('', IssueListView.as_view(), name='issues'),
    path('create_issue', CreateIssueView.as_view(), name='create_issue'),
    path('create_status', CreateStatusView.as_view(), name='create_status'),
    path('issue/<int:pk>', IssueDetailView.as_view(), name='issue'),
    path('update_issue/<int:pk>', UpdateIssueView.as_view(), name='update_issue'),
    path('delete_issue/<int:pk>', DeleteIssueView.as_view(), name='delete_issue'),
]

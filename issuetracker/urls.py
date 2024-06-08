from django.urls import path

from issuetracker import views

urlpatterns = [
    path('', views.IssueListView.as_view(), name='issues'),
    path('projects/create_issue/<int:pk>', views.CreateIssueView.as_view(), name='create_issue'),
    path('create_status', views.CreateStatusView.as_view(), name='create_status'),
    path('issue/<int:pk>', views.IssueDetailView.as_view(), name='issue'),
    path('update_issue/<int:pk>', views.UpdateIssueView.as_view(), name='update_issue'),
    path('delete_issue/<int:pk>', views.DeleteIssueView.as_view(), name='delete_issue'),
    path('projects', views.ProjectListView.as_view(), name='projects'),
    path('projects/project/<int:pk>', views.ProjectDetailView.as_view(), name='project'),
    path('projects/create_project', views.ProjectCreateView.as_view(), name='create_project'),
    path('projects/update_project/<int:pk>', views.ProjectUpdateView.as_view(), name='update_project'),
    path('projects/delete_project/<int:pk>', views.ProjectDeleteView.as_view(), name='delete_project'),
    path('projects/project_team/<int:pk>', views.ProjectTeamView.as_view(), name='project_team'),
    path('projects/add_to_project/<int:pk>', views.AddToProjectView.as_view(), name='add_to_project'),
]

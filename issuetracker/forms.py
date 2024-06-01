from django.forms import ModelForm
from django import forms

from issuetracker.models import Issue, Status, Type, Project


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        exclude = ['created_by', 'updated_by', 'project',]


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ('name',)


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ('name',)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150, required=False, label='Search')


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(ModelForm):
    start = forms.DateField(widget=DateInput(format='%Y-%m-%d'), label='Дата начала')
    deadline = forms.DateField(widget=DateInput(format='%Y-%m-%d'), required=False, label='Дата окончания')

    class Meta:
        model = Project
        exclude = ['user']

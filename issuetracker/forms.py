from django.forms import ModelForm
from django import forms

from issuetracker.models import Issue, Status, Type, Project
from accounts.models import Account


class IssueForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Статус не выбран'
        self.fields['type'].empty_label = 'Тип не выбран'

    class Meta:
        model = Issue
        exclude = ['created_by', 'updated_by', 'project', 'is_deleted']


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
        exclude = ['user', ]


class ProjectAddUserForm(forms.Form):
    user = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Account.objects.all())

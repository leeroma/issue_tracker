from django.forms import ModelForm

from issuetracker.models import Issue, Status, Type


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        exclude = ['created_by', 'updated_by']


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ('name',)


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ('name',)

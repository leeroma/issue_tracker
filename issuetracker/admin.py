from django.contrib import admin

from issuetracker.models import Issue, Status, Type


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary',)
    list_filter = ('type', 'status',)
    search_fields = ('id', 'summary', 'description',)
    exclude = []
    readonly_fields = ('created_at', 'updated_at',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    exclude = []


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    exclude = []


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)

from django.contrib import admin

from accounts.forms import AccountForm
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    search_fields = ('id', 'email', 'first_name', 'last_name',)
    exclude = []
    form = AccountForm


admin.site.register(Account, AccountAdmin)

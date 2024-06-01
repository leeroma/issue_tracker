from django import forms

from accounts.models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, strip=False, required=True)
    password_confirm = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput, strip=False,
                                       required=True, )
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise forms.ValidationError('Необходимо заполнить имя или фамилию')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password', 'password_confirm', ]

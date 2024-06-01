from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from accounts.forms import AccountForm


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('issues')

        context = {'message': 'Invalid email or password'}

        return render(request, self.template_name, context=context)


def logout_view(request):
    logout(request)
    return redirect('issues')


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = AccountForm
    success_url = 'articles'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('issues')

        context = {'form': form}
        return render(request, self.template_name, context=context)

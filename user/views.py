from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.template.response import TemplateResponse
from django.views import View
from .forms import LoginForm






class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):

        if not request.user.is_anonymous:
            return HttpResponseRedirect('/')

        data = request.POST
        print(request.POST)
        user = authenticate(username=data['username'], password=data['password'])

        if user is not None:
            login(request, user)

            return HttpResponseRedirect('/')

        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')



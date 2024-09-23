from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView

from django.contrib.auth import get_user_model
User = get_user_model()

from usuarios.forms import AccountSignupForm

class UserCreateView(CreateView):
    model = User
    template_name = "registration/cadastro.html"
    form_class = AccountSignupForm
    success_url = reverse_lazy("usuarios:login")
    success_mensage = "Cadastro feito com sucesso!"

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_mensage)
        return super(UserCreateView, self).form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = ["username", "password"]
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('biddingContracts:index')  # redireciona para a página inicial após o login
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('biddingContracts:index')
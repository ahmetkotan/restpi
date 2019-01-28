from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from restpi.forms import MyLoginForm

class Index(TemplateView):
    template_name = 'index.html'

class Login(LoginView):
    form_class = MyLoginForm

class Logout(LogoutView):
    next_page = "/login"

# user/views.py

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib import messages

from .forms import UserRegistrationForm, LoginForm

class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/home/'

class UserLoginView(LoginView):           # 로그인
    authentication_form = LoginForm
    template_name = 'user/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)

class UserLogout(TemplateView):
    template_name = ''
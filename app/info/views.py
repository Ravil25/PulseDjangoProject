from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .form import ProfileForm, RegisterUserForm, LoginUserForm, ReportForm
from .models import UserProfile, PulseReport
from .utils import DataMixin


class index(TemplateView, DataMixin):
    template_name = 'info/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная")
        return dict(list(context.items()) + list(c_def.items()))


def add_user(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            try:
                existing_profile = UserProfile.objects.get(user=user)
                existing_profile.name = profile.name
                existing_profile.age = profile.age
                existing_profile.height = profile.height
                existing_profile.weight = profile.weight
                existing_profile.save()
            except UserProfile.DoesNotExist:
                profile.save()

            messages.success(request, 'User was created successfully!')
            login(request, user)
            return redirect('index')

    else:
        user_form = RegisterUserForm()
        profile_form = ProfileForm()
    return render(request, 'info/add_user.html', {'user_form': user_form, 'profile_form': profile_form})


class AddReport(CreateView, DataMixin):
    model = PulseReport
    form_class = ReportForm
    template_name = 'info/add_report.html'
    context_object_name = "objects"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить отчет")
        return dict(list(context.items()) + list(c_def.items()))


class ShowInfo(ListView, DataMixin):
    model = UserProfile
    template_name = 'info/info.html'
    context_object_name = "objects"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить отчет")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'info/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')

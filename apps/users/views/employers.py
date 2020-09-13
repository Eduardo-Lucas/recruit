from allauth.account.views import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView

from apps.users.decorators import employer_required
from apps.users.forms import EmployerSignUpForm, EmployerForm
from apps.users.models import CustomUser, Employer


class EmployerSignUpView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = EmployerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class EmployerUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = '__all__'
    template_name = 'users/employer_form.html'
    success_url = reverse_lazy('home')


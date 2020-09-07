from allauth.account.views import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from apps.users.decorators import jobseeker_required
from apps.users.forms import JobSeekerSignUpForm, JobSeekerForm
from apps.users.models import CustomUser, JobSeeker


class JobSeekersSignUpView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = JobSeekerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'jobseeker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class JobSeekerUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = JobSeekerForm
    template_name = 'users/jobseeker_form.html'
    success_url = reverse_lazy('home')

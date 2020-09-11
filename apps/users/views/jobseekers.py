from allauth.account.views import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
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


def convert_audio_text(request):
    return render(request, 'users/convert_audio_text.html', {})


def audio_text_convertion(request):
    # importing the module
    import speech_recognition as sr
    # define the recognizer
    r = sr.Recognizer()
    # define the audio file
    audio_file = sr.AudioFile('audios/116-288045-0004.flac')
    # speech recognition
    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    result = r.recognize_google(audio)
    # exporting the result
    with open('texts/116-288045-0004.txt', mode='w') as file:
        file.write("Recognized text:")
        file.write("\n")
        file.write(result)
        print("ready!")

    return redirect('convert_audio_text')


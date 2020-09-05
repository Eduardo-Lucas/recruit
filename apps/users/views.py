from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.users.forms import ProfileForm
from apps.users.models import CustomUser


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = ProfileForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        customuser = form.save(commit=False)
        customuser.full_name = self.request.user.first_name + ' ' + self.request.user.last_name
        customuser.save()
        return super(CustomUserUpdateView, self).form_valid(form)

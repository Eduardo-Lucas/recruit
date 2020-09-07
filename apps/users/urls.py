from django.urls import path

from apps.users.views import jobseekers, employers
from apps.users.views.employers import EmployerUpdateView
from apps.users.views.jobseekers import JobSeekerUpdateView
from apps.users.views.users import SignUpView


urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/jobseeker/', jobseekers.JobSeekersSignUpView.as_view(), name='jobseeker_signup'),
    path('accounts/signup/employer/', employers.EmployerSignUpView.as_view(), name='employer_signup'),

    path('edit_jobseeker/<int:pk>', JobSeekerUpdateView.as_view(), name='edit_jobseeker'),
    path('edit_employer/<int:pk>', EmployerUpdateView.as_view(), name='edit_employer')

]

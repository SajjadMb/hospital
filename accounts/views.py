from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView , TemplateView
from django.shortcuts import redirect , render, HttpResponseRedirect

from .forms import DoctorSignUpForm, PatientSignUpForm , RegisterForm, ProfileForm
from .models import Patient, Doctor, Profile


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ResetPassword(TemplateView):
    template_name = 'registration/password_reset_form.html'


class DoctorSignUpView(CreateView):
    model = Doctor
    form_class = DoctorSignUpForm
    template_name = 'registration/doctor_signup_form.html'
    context_object_name = 'doctor_form'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def doctor_sign_up_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, prefix='register')
        doctor_form = DoctorSignUpForm(request.POST, prefix='doctor-form')
        profile_form = ProfileForm(request.POST, prefix='profile-form')
        if register_form.is_valid() and doctor_form.is_valid() and profile_form.is_valid():
            user = register_form.save()
            profile = Profile(user_id=user.id,
                              birth_date=profile_form.cleaned_data['birth_date'],
                              bio=profile_form.cleaned_data['bio'],
                              sex=profile_form.cleaned_data['sex'],
                              phone_number=profile_form.cleaned_data['phone_number'],
                              location=profile_form.cleaned_data['location'])
            profile.save()
            doctor = Doctor(user_id=user.id,
                            specifications=doctor_form.cleaned_data['specifications'],
                            personal_num=doctor_form.cleaned_data['personal_num'])
            doctor.save()
            login(request, user)
            return redirect("home")
        else:
            print("one of the forms is invalid")
    else:
            register_form = RegisterForm(prefix='register')
            doctor_form = DoctorSignUpForm(prefix='doctor-form')
            profile_form = ProfileForm(prefix='profile-form')
    return render(request, 'registration/doctor_signup_form.html', {
        'register': register_form,
        'doctorForm': doctor_form,
        'profileForm': profile_form,
    })


class PatientSignUpView(CreateView):
    model = Patient
    form_class = PatientSignUpForm
    template_name = 'registration/patient_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def patient_sign_up_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, prefix='register')
        patient_form = PatientSignUpForm(request.POST, prefix='patient-form')

        if register_form.is_valid() and patient_form.is_valid():
            user = register_form.save()
            patient_form.cleaned_data["user"] = user
            patient_form.save()
            login(request, user)
            return redirect("home")
        else:
            print("one of the forms is invalid")
    else:
            register_form = RegisterForm(prefix='register')
            patient_form = DoctorSignUpForm(prefix='patient-form')

    return render(request, 'registration/patient_signup_form.html', {
        'register': register_form,
        'doctorForm': patient_form,
    })
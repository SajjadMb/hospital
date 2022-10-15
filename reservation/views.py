from django.shortcuts import  redirect , render , reverse
from django.views.generic import TemplateView
from .forms import SearchDoctorForm,ReservationForm
from django.views.generic.edit import FormView
from accounts.models import Doctor
from .models import Reservation
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
class searchDoctor(FormView):
    template_name = 'reservation/search.html'
    form_class= SearchDoctorForm

    def get(self, request,*args,**kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            specification = form.cleaned_data['specifications']
            qs = Doctor.objects.filter(specifications = specification)
            username = qs.model.user
            return redirect('appointment', {'qs':qs})

        return render(request, self.template_name, {'form': form})



class appointment(FormView):
    template_name = 'reservation/appointment.html'
    form_class = ReservationForm

    def get(self, request,*args,**kwargs):
        #user = request.GET.get('username','')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            qs_count = Doctor.objects.filter(reservation_date = reservation_date).count()
            if qs_count >= 2 :
                return HttpResponse("try to attempt later")
            else:
                reservation = Reservation()
            # redirect('appointment', {'qs':qs})

        return render(request, self.template_name, {'form': form})




    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})
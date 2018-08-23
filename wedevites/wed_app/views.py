from django.shortcuts import render
from django.views.generic import (TemplateView)

from wed_app.forms import (RSVPForm,UserLoginForm)
from wed_app.models import Guest


# Create your views here.

def login_view(request):
    form = UserLoginForm()

    if request.method == 'POST':

        form = UserLoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            print(username)
            return render(request,'confirmation.html',{'form': form, 'username':username})
            # return rsvp(request)
        else:
            print('ERROR form invalid')

    return render(request, 'form.html', {'form':form})


class JoiePaulofLoveView(TemplateView):
    template_name = 'JoiePaulofLove.html'

class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'

class HomeView(TemplateView):
    template_name = 'base.html'

class RSVPView(TemplateView):
    template_name = 'rsvp.html'

def rsvp(request):
    return render(request, 'confirmation.html')


def guests(request):
    form = RSVPForm()

    if request.method == 'POST':

        form = RSVPForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            guest = Guest.objects.latest('date')
            print(guest)
            return render(request,'confirmation.html',{'form': form, 'guest':guest.name})
            # return rsvp(request)
        else:
            print('ERROR form invalid')

    return render(request, 'form.html', {'form':form})



from django.shortcuts import render,redirect
from .forms import SubscribeForm

from subscribe.models import Subscribs
from django.urls import reverse


# Create your views here.


# def subscribes(request):
#     subscribe_form = SubscribeForm()
#     context ={}
#     email_error = ''
#     email = ''
#     if request.POST :
#         subscribe_form = SubscribeForm(request.POST)
#         if subscribe_form.is_valid():
#             print(subscribe_form.cleaned_data)
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST["last_name"]
#         if email == "":
#             email_error = "email is empty"
#             context['email_error'] = email_error

#             return render(request,'subscribe/subscribs.html',context)

#         if Subscribs.objects.filter(email=email):
#             email_error = "This email already exits"
#             context['email_error'] = email_error
#             return render(request,'subscribe/subscribs.html',context)
#         else:
#             Subscribe = Subscribs(first_name=first_name,last_name = last_name,
#                     email = email)
#             Subscribe.save()
#             return redirect(reverse('thank_you'))

#     context = {'email_error':email_error,'form':subscribe_form}
#     return render (request,'subscribe/subscribs.html',context)
# Create your views here.
def subscribes(request):
    subscribe_form = SubscribeForm()
    email_error_empty=""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('thank_you'))
    context={"form": subscribe_form,"email_error_empty":email_error_empty}
    return render(request, 'subscribe/subscribs.html', context)



def thank_you(request):
    context = {}
    return render (request,'subscribe/thank_you.html',context)
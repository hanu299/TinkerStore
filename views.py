from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():			
            name = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, number, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact_us/email.html", {'form': form})


def success(request):
    	return HttpResponse("Thank YOU So Much, We Will Get Back To You In 2day Working Days!")

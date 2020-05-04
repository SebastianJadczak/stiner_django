from django.core.mail import send_mail
from django.shortcuts import render

from contact.forms import EmailForm


def post_share(request):
    sent= False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(form,['sebastian-jadczak@wp.pl'])
            cd = form.cleaned_data
            sent=True
    else:
        form = EmailForm()

    return render(request,'contact/contact.html',{'form':form, 'sent':sent})
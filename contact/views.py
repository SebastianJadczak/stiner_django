from django.core.mail import send_mail
from django.shortcuts import render

from contact.forms import EmailForm
from shop.models import Category


def post_share(request):
    category = Category.objects.all()
    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['name'], cd['comments'], ['aaaaaaaaa@a.pl'], ['sebastian-jadczak@wp.pl'])
            sent = True
    else:
        form = EmailForm()

    return render(request, 'contact/contact.html', {'form': form, 'sent': sent, 'category': category})

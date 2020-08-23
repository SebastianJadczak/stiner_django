from django.shortcuts import render
from django.views.generic.base import View


class UserAccount(View):
    template_name = 'account/user_account.html'

    def get(self, request):
        return render(request, self.template_name)
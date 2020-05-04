from django.shortcuts import render
from django.views import View


class Trails(View):
    template_name= 'trails/trails.html'

    def get(self, request):
        return render(request, self.template_name)

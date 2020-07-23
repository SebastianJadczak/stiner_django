from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from map.models import Point
from trails.models import Trail


class UserTrailsListView(ListView):
    template_name = 'trails/user_trails/user_trails.html'
    model = Trail


class UserTrailFormAdd(TemplateView):
    template_name ='trails/user_trails/form_trails.html'


    def get_context_data(self, **kwargs):
        context = super(UserTrailFormAdd, self).get_context_data(**kwargs)
        context['lists'] = Point.objects.all()
        return context

class AddPointToTrail(object):

    def __init__(self, request):
        """ inicjalizacja tworzenia tras """

        self.session = request.session
        trail = self.session.get(settings.AddPointToTrail_SESSION_ID)
        if not trail:
            trail = self.session[settings.AddPointToTrail_SESSION_ID] = {}
        self.trail = trail

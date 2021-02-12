from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from map.models import Point, Coordinates
from user_trails.models import UserTrail, UserPoint
from .forms import UserTrailCreateForm


class UserTrailsListView(ListView):
    """Klasa odpowiedzialna za wyświetlenie widoku Tras zwiedzania użytkowników"""
    template_name = 'trails/user_trails/user_trails.html'
    model = UserTrail
    your_list_trails = []

    def post(self, request, *args, **kwargs):
        self.your_list_trails.clear()
        for key, value in request.POST.items():
            if 'name' in key:
                self.your_list_trails.append(UserTrail.objects.filter(name__contains=value))
            if 'country' in key:
                self.your_list_trails.append(UserTrail.objects.filter(country=value))
            if 'region' in key:
                self.your_list_trails.append(UserTrail.objects.filter(region__contains=value))
            if 'city' in key:
                self.your_list_trails.append(UserTrail.objects.filter(city__contains=value))
        return redirect('../user_trails/search_user_trails/',
                        {'list': self.your_list_trails})

    def get_city(self):
        city = list(Coordinates.objects.all())
        return city

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_trails'] = UserTrail.objects.filter(user=self.request.user)
        context['user_trails_point'] = UserPoint.objects.all()
        context['city'] = self.get_city()
        return context

class SearchUserTrails(UserTrailsListView):
    """Klasa odpowiedzialna za wyświetlenie wyników wyszukania tras użytkownika."""
    template_name = 'trails/user_trails/search_user_trails.html'
    model = UserTrail

class UserTrailFormAdd(ListView):
    """Klasa odpowiedzialna za wyświetlenie obiektów które możesz dodasz do szkicu trasy"""
    template_name = 'trails/user_trails/form_trails.html'
    model = Point
    list = Point.objects.all()
    user_trail = []
    zmienna = ""
    city = Coordinates.objects.all()

    def checkQueryinUserDraftTrail(self, query):
        for a in self.user_trail:
            for z in a:
                if query == str(z):
                    return False

    def get(self, request, *args, **kwargs):

        query = request.GET.get('add_point')
        if query:
            result = self.checkQueryinUserDraftTrail(query)
            if result == False:
                self.zmienna += "Nie możesz dodać tego zabytku. Istnieje już w bazie"
            else:
                self.user_trail.append(self.list.filter(name=query))
        len_user = len(self.user_trail)

        return render(request, self.template_name,
                      {'list': self.list,'city':self.city, 'user_trail': self.user_trail, 'len_user': len_user, 'zmienna': self.zmienna})


class UserTrailDraft(UserTrailFormAdd):
    """Klasa odpowiedzialna za Szkic trasy zwiedzania"""
    template_name = 'trails/user_trails/draft/trail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        query = request.GET.get('delete')
        if query:
            for z in self.user_trail:
                for i in z:
                    if i.name == query:
                        self.user_trail.remove(z)
                        break

        return render(request, self.template_name, {'list': self.list, 'user_trail': self.user_trail, 'zmienna': self.zmienna})


class DetailPoint(DetailView):
    template_name = 'trails/user_trails/detail.html'
    model = Point

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SaveDraftTrailUser(UserTrailFormAdd):
    template_name = 'trails/user_trails/draft/save_draft_trail.html'

    def clear_board_user(self):
        del self.user_trail[:]

    def get(self, request):
        form = UserTrailCreateForm()
        return render(request, self.template_name, {'form': form, 'user_trail': self.user_trail})

    def post(self, request):
        form = UserTrailCreateForm(request.POST)
        if form.is_valid():
            user_trail_draft = form.save(commit=False)
            user_trail_draft.user = User.objects.get(username=request.user)
            user_trail_draft.save()
            for items in self.user_trail:
                for item in items:
                    UserPoint.objects.create(trails=user_trail_draft,
                                             name=item.name,
                                             descriptions=item.descriptions,
                                             location=item.location,
                                             coordinateX=item.coordinateX,
                                             coordinateY=item.coordinateY,
                                             image=item.image,
                                             type=item.type)
            self.clear_board_user()
            return render(request, 'trails/user_trails/form_trails.html', {'form': form, 'user_trail': self.user_trail})


class UserTrailDetail(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'trails/user_trails/user_trail_detail.html'
    model = UserTrail

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_trail'] = list(UserTrail.objects.filter(id=self.kwargs['pk']))[0]
        context['user_trail_id'] = self.kwargs['pk']
        # context['points'] =list(list(UserTrail.objects.filter(id=self.kwargs['pk']))[0].points.all())
        return context


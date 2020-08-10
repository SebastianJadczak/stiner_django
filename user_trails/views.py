from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from map.models import Point
from trails.models import Trail
from user_trails.models import UserTrail, UserPoint
from .forms import UserTrailCreateForm


class UserTrailsListView(ListView):
    """Klasa odpowiedzialna za wyświetlenie widoku Tras zwiedzania użytkowników"""
    template_name = 'trails/user_trails/user_trails.html'
    model = UserTrail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_trails'] = UserTrail.objects.filter(user=self.request.user)
        return context


class UserTrailFormAdd(ListView):
    """Klasa odpowiedzialna za wyświetlenie obiektów które możesz dodasz do szkicu trasy"""
    template_name = 'trails/user_trails/form_trails.html'
    model = Point
    list = Point.objects.all()
    user = []
    zmienna = ""

    def checkQueryinUserDraftTrail(self, query):
        for a in self.user:
            for z in a:
                if query == str(z):
                    return False

    def get(self, request, *args, **kwargs):
        request.GET._mutable = True
        query = request.GET.get('add_point')
        if query:
            result = self.checkQueryinUserDraftTrail(query)
            if result == False:
                self.zmienna += "Nie możesz dodać tego zabytku. Istnieje już w bazie"
            else:
                self.user.append(self.list.filter(name=query))
        len_user = len(self.user)

        return render(request, self.template_name,
                      {'list': self.list, 'user': self.user, 'len_user': len_user, 'zmienna': self.zmienna})


class UserTrailDraft(UserTrailFormAdd):
    """Klasa odpowiedzialna za Szkic trasy zwiedzania"""
    template_name = 'trails/user_trails/draft/trail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        query = request.GET.get('delete')
        if query:
            for z in self.user:
                for i in z:
                    if i.name == query:
                        self.user.remove(z)
                        break

        return render(request, self.template_name, {'list': self.list, 'user': self.user, 'zmienna': self.zmienna})


class DetailPoint(DetailView):
    template_name = 'trails/user_trails/detail.html'
    model = Point

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SaveDraftTrailUser(UserTrailFormAdd):
    template_name = 'trails/user_trails/draft/save_draft_trail.html'

    def clear_board_user(self):
        del self.user[:]

    def get(self, request):
        form = UserTrailCreateForm()
        return render(request, self.template_name, {'form': form, 'user': self.user})

    def post(self, request):
        form = UserTrailCreateForm(request.POST)
        if form.is_valid():
            user_trail = form.save(commit=False)
            user_trail.user = User.objects.get(username=request.user)
            user_trail.save()
            for items in self.user:
                for item in items:
                    UserPoint.objects.create(trails=user_trail,
                                             name=item.name,
                                             descriptions=item.descriptions,
                                             location=item.location,
                                             coordinateX=item.coordinateX,
                                             coordinateY=item.coordinateY,
                                             image=item.image,
                                             type=item.type)
            self.clear_board_user()
            return render(request, 'trails/user_trails/user_trails.html', {'form': form, 'user': self.user})
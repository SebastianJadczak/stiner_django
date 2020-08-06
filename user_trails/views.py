from django.shortcuts import render

from django.views.generic import ListView, DetailView

from map.models import Point
from trails.models import Trail
from user_trails.models import UserTrail
from .forms import UserTrailCreateForm


class UserTrailsListView(ListView):
    """Klasa odpowiedzialna za wyświetlenie widoku Tras zwiedzania użytkowników"""
    template_name = 'trails/user_trails/user_trails.html'
    model = Trail


class UserTrailFormAdd(ListView):
    """Klasa odpowiedzialna za wyświetlenie obiektów które możesz dodasz do szkicu trasy"""
    template_name ='trails/user_trails/form_trails.html'
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
                self.zmienna+="Nie możesz dodać tego zabytku. Istnieje już w bazie"
            else:
                self.user.append(self.list.filter(name=query))
        len_user = len(self.user)

        return render(request, self.template_name,
                      {'list': self.list, 'user':self.user, 'len_user':len_user, 'zmienna':self.zmienna })

class UserTrailDraft(UserTrailFormAdd):
    """Klasa odpowiedzialna za Szkic trasy zwiedzania"""
    template_name = 'trails/user_trails/draft/trail.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self,request, *args, **kwargs):
        query = request.GET.get('delete')
        if query:
            for z in self.user:
                for i in z:
                    if i.name == query:
                        self.user.remove(z)
                        break

        return render(request, self.template_name, {'list': self.list, 'user':self.user, 'zmienna':self.zmienna })

class DetailPoint(DetailView):
    template_name = 'trails/user_trails/detail.html'
    model = Point

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def SaveDraftTrailUser(request):
    """Widok odpowiedzialny za wyświetlenie formularza i zapisu trasy użytkownika."""

    template_name = 'trails/user_trails/draft/save_draft_trail.html'

    if request.method == 'POST':
        form = UserTrailCreateForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UserTrailCreateForm()

    return render(request, template_name, {'form': form})
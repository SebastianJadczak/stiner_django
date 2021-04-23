from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Profile, Preference


class UserAccount(View):
    template_name = 'account/user_account.html'

    def get(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        preference = Preference.objects.filter(user=request.user).first()
        if profile is None:
            average = 0
            return render(request, self.template_name, {"średnia": average})
        else:
            table_profile = [(field.name, getattr(profile, field.name)) for field in profile._meta.fields]
            table_preference = [(field.name, getattr(preference, field.name)) for field in preference._meta.fields]

            sum_fields = (len(table_profile) + len(table_preference) - 4)
            filled_in_fields = 0
            for field, value in (table_profile + table_preference):
                filled_in_fields += 1 if value != '' and field != 'id' and field != 'user' else 0

            average = round((filled_in_fields / sum_fields) * 100)
            return render(request, self.template_name, {"średnia": average, "fullname": profile.full_name(),
                                                        "date_of_birth": profile.date_of_birth_user(),
                                                        "contact_colors_star": profile.contact_fields_filled(),
                                                        'address_fields_filled': profile.address_fields_filled(),
                                                        'language_fields_filled': profile.language_fields_filled(),
                                                        'preference_fields_filled': preference.preference_fields_filled(),
                                                        })

    def post(self, request):
        "Profile."
        profile = Profile.objects.filter(user=request.user).first()
        profile.name = request.POST.get('name')
        profile.surname = request.POST.get('surname')
        profile.date_of_birth = request.POST.get('date_of_birth')
        profile.photo = request.POST.get('photo')
        profile.country = request.POST.get('country')
        profile.city = request.POST.get('city')
        profile.street = request.POST.get('street')
        profile.house_number = request.POST.get('house_number')
        profile.apartment_number = request.POST.get('apartment_number')
        profile.postal_code = request.POST.get('postal_code')
        profile.main_language = request.POST.get('main_language')
        profile.other_language = request.POST.get('other_language')
        profile.phone = request.POST.get('phone')
        profile.email = request.POST.get('email')
        profile.save()
        "Preference."
        preference = Preference.objects.filter(user=request.user).first()
        preference.favorite_country = request.POST.get('favorite_country')
        preference.favorite_region = request.POST.get('favorite_region')
        preference.favorite_city = request.POST.get('favorite_city')
        preference.favorite_place = request.POST.get('favorite_place')
        preference.favorite_restaurant = request.POST.get('favorite_restaurant')
        preference.save()
        return redirect('./my_account')

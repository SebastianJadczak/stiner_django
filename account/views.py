from django.shortcuts import render
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
            print(profile.contact_fields_filled())
            return render(request, self.template_name, {"średnia": average, "fullname": profile.full_name(),
                                                        "date_of_birth": profile.date_of_birth_user(),
                                                        "contact_colors_star": profile.contact_fields_filled(), })

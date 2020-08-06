
from django.urls import path


from . import views


app_name = 'user_trails'



urlpatterns = [
    path('user_trails_add', views.UserTrailFormAdd.as_view(), name='user_trail_add'),
    path('detail_point/<int:pk>/', views.DetailPoint.as_view(), name='detail_point'),
    path('user_trail_draft/', views.UserTrailDraft.as_view(), name='user_trail_draft'),
    path('save_draft_trail/', views.SaveDraftTrailUser, name='save_draft_trail'),
]


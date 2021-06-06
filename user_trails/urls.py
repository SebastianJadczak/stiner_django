
from django.urls import path


from . import views


app_name = 'user_trails'



urlpatterns = [
    path('user_trails_add', views.UserTrailFormAdd.as_view(), name='user_trail_add'),
    path('detail_point/<int:pk>/', views.DetailPoint.as_view(), name='detail_point'),
    path('user_trail_draft/', views.UserTrailDraft.as_view(), name='user_trail_draft'),
    path('save_draft_trail/', views.SaveDraftTrailUser.as_view(), name='save_draft_trail'),
    path('search_user_trails/', views.SearchUserTrails.as_view(), name='search_user_trails'),
    path('user_trail_detail/<int:pk>/', views.UserTrailDetail.as_view(), name='user_trail_detail'),
    path('api/<int:pk>', views.TrailUserApiFilterListView.as_view()),
    path('test/', views.AddToTrail.as_view(), name='test'),
    path('pdf_your_trail/<int:pk>', views.trail_render_pdf_view, name='pdf_your_trail'),
    path('user_trail_detail/<int:pk>/audioCount/', views.UserTrailDetail.audioCount, name='audioCount')
]


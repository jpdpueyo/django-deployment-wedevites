from django.conf.urls import url
from wed_app import views
from wed_app.views import (login_view)


urlpatterns = [
    url(r'^$',views.JoiePaulofLoveView.as_view(),name='index'),
    url(r'^joiepauloflove/$',views.JoiePaulofLoveView.as_view(),name='JoiePaulofLove'),
    url(r'^rsvp/$',views.RSVPView.as_view(),name='rsvp'),
    url(r'^rsvpform/$',views.guests,name='rsvpform'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^confirmation/$',views.ConfirmationView.as_view(),name='confirmation'),

]

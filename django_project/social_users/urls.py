# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from .views import UserSigninPage, UserProfilePage, LogoutUser, ProfilePage

urlpatterns = patterns(
    '',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^signin/$', UserSigninPage.as_view(), name='usersignpage'),
    url(r'^profile/$', UserProfilePage.as_view(), name='userprofilepage'),
    url(
        r'^profile/(?P<username>.*)/$', ProfilePage.as_view(),
        name='profile'
    ),
    url(r'^logout/$', LogoutUser.as_view(), name='logout_user'),
    url(
        r'^user/updates/$',
        'social_users.views.get_user_updates',
        name='user-updates'
    ),
)

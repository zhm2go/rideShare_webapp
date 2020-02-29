"""rideShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from ride.views import *
from accouts.views import signup, my_account, edit_email
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^signup/$', signup, name = 'signup'),
    re_path('^logout/$', LogoutView.as_view(), name = 'logout'),
    re_path('^login/$', LoginView.as_view(template_name='login.html'), name = 'login'),
    re_path('^new_ride/$', new_ride, name = 'new_ride'),
    re_path('^ride_requested/$', ride_made, name = 'ride_requested'),
    re_path('^ride_delete/(?P<pk>\d+)/$', delete_ride, name = 'delete_ride'),
    re_path('^ride_modify/(?P<pk>\d+)/$', modify_ride, name = 'modify_ride'),
    re_path('^new_share/$', new_share, name = 'new_share'),
    re_path('^share_requested/$', share_made, name = 'share_requested'),
    re_path('^delete_share/(?P<pk>\d+)/$', delete_share, name = 'delete_share'),
    re_path('^search_ride/(?P<pk>\d+)/$', search_ride, name = 'search_ride'),
    re_path('^join_ride/$', join_ride, name = 'join_ride'),
    re_path('^modify_share/(?P<pk>\d+)/$', modify_share, name = 'modify_share'),
    re_path('^owner_details/(?P<pk>\d+)/$', owner_details, name = 'owner_details'),
    re_path('^share_details/(?P<pk>\d+)/$', share_details, name = 'share_details'),
    re_path('^new_driver/$', new_driver, name = 'new_driver'),
    re_path('^driver_info/$', driver_info, name = 'driver_info'),
    re_path('^modify_driver/$', drive_modify, name = 'modify_driver'),
    re_path('^delete_drive/$', delete_driver, name = 'delete_drive'),
    re_path('^search_drive/$', driver_search, name = 'driver_search'),
    re_path('^confirm_ride/(?P<pk>\d+)/$', confirm_ride, name = 'driver_confirm'),
    re_path('^check_confiremed_ride/$', check_confirmed_ride, name = 'check_confiremed_ride'),
    re_path('^driver_complete/$', driver_complete, name = 'driver_complete'),
    re_path('^view_driver_details/$', view_driver_detail, name = 'view_driver_detail'),
    re_path('^my_account/$', my_account, name = 'my_account'),
    re_path('^change_email/$', edit_email, name = 'edit_email'),
    re_path('^$', home, name = 'home'),

    re_path('^base', base),
]
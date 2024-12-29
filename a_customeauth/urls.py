from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import login_view, profile_view,register_view,logout_view


urlpatterns = [
    path('login/',login_view,name='auth_login'),
    path('register/',register_view,name='auth_register'),
    path('profile/',profile_view,name='auth_profile'),
    path('logout/',logout_view,name='auth_logout'),
]


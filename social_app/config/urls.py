from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from faceb_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.index, name="home"),
]
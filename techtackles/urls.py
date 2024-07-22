from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf.urls import handler404
from .views import custom_404_view
from support.views import custom_login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include("support.urls"), name="support-urls"),
    path("accounts/", include("allauth.urls")),
    path('login/', custom_login_view, name='custom_login'),

]

handler404 = custom_404_view

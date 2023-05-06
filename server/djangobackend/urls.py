"""djangobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static, serve
from django.conf import settings

from rest_framework.routers import DefaultRouter

# import api.views
# import ugc.views
# import twofactorauth.views
# router = DefaultRouter()
# router.register(r'packages', api.views.PackageViewSet)
# router.register(r'public/packages', api.views.PublicPackageViewSet)
# router.register(r'bookings', api.views.BookingViewSet)
# router.register(r'journal', ugc.views.JournalViewSet)


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('../../functions/.env'))

urlpatterns = [
    path(os.environ.get('ADMIN') + "/admin/", admin.site.urls),
    # djangpapp
    path('', include('djangoapp.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

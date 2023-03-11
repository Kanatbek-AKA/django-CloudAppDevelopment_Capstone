from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path("about_us/", views.about, name="about_us"),
    # path for contact us view
    path("djangoapp/contact_us/", views.contact, name="contact_us"),
    # path for registration
    # path("registration/", views.registration, name="registration"),
    # path for login
    # path("login/", views.login, name="login"),
    # path for logout
    # path("logout/", views.logout, name="logout"),
    # path  
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'djangoapp'
urlpatterns = [
    # Pure cloud according IBM staffs recomendation
    path(route='', view=views.IndexPageView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path("error_page/", views.ErrorPage.as_view(), name="errors"),
    path('new_dealer/', views.NewDealerMember.as_view(), name='members'),
    path("about_us/", views.AboutPageView.as_view(), name="about"),
    path("dealerships/", views.DealerPageView.as_view(), name="dealerships"),
    path("reviews/", views.AddReviewView.as_view(), name="reviews"),
    path("contact_us/", views.ContactPageView.as_view(), name="contact"),

    # Course using local SQlite
    # path(route='', view=views.get_dealerships, name='index'),
    # path("dealerships/<int:dealer_id>/ ", views.DealerPageView.as_view(), name="dealerships"),
    # path("reviews/<int:dealer_id>/review/ ", views.AddReviewView.as_view(), name="reviews"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

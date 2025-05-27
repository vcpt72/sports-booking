# facility/urls.py
from django.urls import path
from . import views
from .views import contact_view
from .api import api

urlpatterns = [
    path('', views.index, name='index'),
    # SportFacilities
    
    path('facility/<int:pk>/', views.facility_detail, name='facility_detail'),# detail sportoviště
    path('facility/<int:pk>/reserve/', views.reservation_create, name='reservation_create'),
    path('', views.index, name='index'),  # Hlavní stránka
    path('sportoviste/', views.index, name='index'),  # Sportoviště sekce
    path('o-nas/', views.index, name='index'), # O nas sekce
    path('facility/<int:pk>/reviews/', views.facility_reviews, name='facility_reviews'), # recenze sportoviště
    path('kontakt/', contact_view, name='contact'), # Kontaktní formulář
    path('registrace/', views.register, name='register'), # Registrace uživatele
    path('prihlaseni/', views.user_login, name='login'),    # Přihlášení uživatele
    path('odhlaseni/', views.user_logout, name='logout'),  # Odhlášení uživatele
    path('profil/', views.user_profile, name='user_profile'), # Uživatelský profil
    path('reservations/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'), # Editace rezervace
    path('reservations/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'), # Smazání rezervace
    path('my-reservations/', views.user_reservations, name='user_reservations'),
    path("api/", api.urls),
    ]
from django.contrib import admin
from .models import SportFacility, Reservation, UserProfile, Pricing, FacilityType, Review

admin.site.register(SportFacility)
admin.site.register(Reservation)
admin.site.register(UserProfile)
admin.site.register(Pricing)
admin.site.register(FacilityType)
admin.site.register(Review)
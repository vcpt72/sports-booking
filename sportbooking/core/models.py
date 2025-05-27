from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save

class FacilityType(models.Model):
    name = models.CharField(max_length=100)  # Název typu sportoviště (např. tenis, fotbal)
    description = models.TextField(blank=True)  # Popis typu sportoviště

    def __str__(self):
        return self.name

# Model pro sportoviště
class SportFacility(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(FacilityType, on_delete=models.CASCADE)  # Cizí klíč na FacilityType
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='sport_facilities/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Sport Facilities"

    def __str__(self):
        return self.name

# Model pro rezervace
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Uživatel, který rezervuje
    facility = models.ForeignKey(SportFacility, on_delete=models.CASCADE)  # Sportoviště, které je rezervováno
    date = models.DateField()  # Datum rezervace
    start_time = models.TimeField()  # Začátek rezervace
    end_time = models.TimeField()  # Konec rezervace

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.date} from {self.start_time} to {self.end_time}"

# Model pro uživatelský profil
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # OneToOne vztah s modelem User
    phone_number = models.CharField(max_length=15, blank=True)  # Telefonní číslo
    address = models.TextField(blank=True)  # Adresa uživatele

    def __str__(self):
        return f"Profile of {self.user.username}"

# Model pro ceníky
class Pricing(models.Model):
    facility = models.ForeignKey(SportFacility, on_delete=models.CASCADE)  # Sportoviště, pro které je ceník
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)  # Cena za hodinu

    def __str__(self):
        return f"{self.facility.name} - {self.price_per_hour} per hour"


# Model pro recenze
class Review(models.Model):
    facility = models.ForeignKey('SportFacility', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}/5"
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


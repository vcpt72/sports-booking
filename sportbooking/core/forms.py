from django import forms
from .models import SportFacility, Reservation, Review
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        self.facility = kwargs.pop('facility', None)  # Předáme sportoviště
        self.user = kwargs.pop('user', None)  # Předáme uživatele
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if date and start_time and end_time:
            existing_reservation = Reservation.objects.filter(
                facility=self.facility,
                date=date,
                start_time__lt=end_time,  # Start time is before end time
                end_time__gt=start_time   # End time is after start time
            )
            if existing_reservation.exists():
                raise ValidationError('Tento čas je již zarezervován. Zvolte jiný čas.')

        return cleaned_data
    


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Napište recenzi'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Jméno',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Zpráva',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Tento email je již používán.')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
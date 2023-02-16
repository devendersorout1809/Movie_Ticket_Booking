from django import forms
from .models import *


class TheaterForm(forms.ModelForm):

    class Meta:
        model = Theater
        fields = "__all__"


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = "__all__"


class HallForm(forms.ModelForm):

    class Meta:
        model = Hall
        fields = "__all__"


class ShowForm(forms.ModelForm):

    class Meta:
        model = Show
        fields = "__all__"


class SeatForm(forms.ModelForm):

    class Meta:
        model = Seat
        fields = "__all__"


class BookTicketForm(forms.ModelForm):

    class Meta:
        model = BookTicket
        fields = '__all__'


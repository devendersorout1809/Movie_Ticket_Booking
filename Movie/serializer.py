from rest_framework import serializers
from .models import *
from .forms import *


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


# class HallSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hall
#         fields = '__all__'
#
#
# class ShowSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Show
#         fields = '__all__'
#
#
# class SeatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Seat
#         fields = '__all__'


class BookTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTicket
        fields = '__all__'

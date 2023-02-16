from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')


def theater(request):
    dataa = Theater.objects.all()
    return render(request, 'theater.html', {'data': dataa})


def movies(request):
    dataa = Movie.objects.all()
    return render(request, 'movie.html', {'data': dataa})


def hall(request):
    dataa = Hall.objects.all()
    return render(request, 'hall.html', {'data': dataa})


def show(request):
    dataa = Show.objects.all()
    return render(request, 'show.html', {'data': dataa})


def seat(request):
    dataa = Seat.objects.all()
    return render(request, 'seat.html', {'data': dataa})

def book_ticket(request):
    if request.method == 'POST':
        # Get the selected values from the dropdowns
        theater_name = request.POST.get('theater')
        movie_name = request.POST.get('movie')
        hall_number = request.POST.get('hall')
        seat_number = request.POST.get('seat')

        # Retrieve the corresponding model instances for the selected values
        theater = Theater.objects.get(name=theater_name)
        movie = Movie.objects.get(name=movie_name)
        hall = Hall.objects.get(number=hall_number)
        seat = Seat.objects.get(number=seat_number)

        ticket = BookTicket.objects.create(theater=theater, movie=movie, hall=hall, seat=seat)
        return redirect('/')
    else:
        theaters = Theater.objects.all()
        movies = Movie.objects.all()
        halls = Hall.objects.all()
        seats = Seat.objects.all()
        context = {
            'theater': theaters,
            'movie': movies,
            'hall': halls,
            'seat': seats,
        }
        return render(request, 'bookSeat.html', context)


class TheaterApi(APIView):

    def delete(self, request, id=None):
        dataa = BookTicket.objects.get(id=id)
        dataa.delete()
        return Response({'status': 'success'})

    def get(self, request, *args, **kwargs):
        dataa = BookTicket.objects.all()
        ser = BookTicketSerializer(dataa, many=True)
        return Response({'status': 'success Fetch', 'data': ser.data})

    def post(self, request):
        dataa = BookTicketSerializer(data=request.data)
        if dataa.is_valid():
            dataa.save()
            return Response({'status': 'success insert', 'data': dataa.data})
        return Response({'status': 'Error', 'data': dataa.errors})

    def put(self, request, id=None):
        modData = BookTicket.objects.get(id=id)
        ser = BookTicketSerializer(modData, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'status': 'success insert', 'data': ser.data})
        return Response({'status': 'Error', 'data': ser.errors})










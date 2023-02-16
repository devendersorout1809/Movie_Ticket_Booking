from django.db import models

from django.db import models


class Theater(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hall(models.Model):
    number = models.PositiveIntegerField()
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)

    def __str__(self):
        return f"Hall No {self.number}"


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.name} at {self.hall.number} on {self.start_time}"


class Seat(models.Model):
    row = models.IntegerField()
    number = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)


    def __str__(self):
        return f"Row:{self.row} and Seat no {self.number}"


class BookTicket(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)

    def __str__(self):
        return "Book tickets"


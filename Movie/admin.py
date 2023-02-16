from django.contrib import admin
from Movie.models import *


class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'theater')


class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'theater')


class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'start_time')


class SeatAdmin(admin.ModelAdmin):
    list_display = ('row', 'number', 'hall')


class BookTicketAdmin(admin.ModelAdmin):
    list_display = ('theater', 'movie', 'hall', 'seat')


admin.site.register(Theater, TheaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(BookTicket, BookTicketAdmin)

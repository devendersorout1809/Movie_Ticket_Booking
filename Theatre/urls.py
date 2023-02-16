from django.contrib import admin
from django.urls import path
from Movie import views
from Movie.views import TheaterApi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('theater', views.theater, name='theater'),
    path('movies', views.movies, name='movies'),
    path('hall', views.hall, name='hall'),
    path('show/', views.show, name='show'),
    path('seats', views.seat, name='seats'),
    path('bookTicket', views.book_ticket, name='bookTicket'),
    # FOR API
    path('myapi/<int:id>', TheaterApi.as_view()),
    path('myapi/', TheaterApi.as_view())
]

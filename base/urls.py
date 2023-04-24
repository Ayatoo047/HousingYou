from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='landing'),
    path('houses/', views.all_houses, name ='houses'),
    path('bookings/', views.booking, name ='bookings'),
    # path('book/<str:pk>', views.book_house, name ='book'),
    path('house/<str:pk>', views.house, name ='house'),
]
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from . import *


def index(request):
    return render(request, 'landingpage.html')


def searchHouses(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # tags = Tags.objects.filter(name__icontains=search_query)

    houses = House.objects.distinct().filter(
        Q(type__house_type__icontains=search_query) |
        Q(location__location__icontains=search_query) |
        Q(conpletion_status__title__icontains=search_query)
    )

    return houses, search_query

def paginateHouses(request, houses, results):
    page = request.GET.get('page')
    # results = 3
    paginator = Paginator(houses, results)

    try:
        houses = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        houses = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        houses = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex =(int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    # projects = paginator.page(page)
    custom_range = range(leftIndex, rightIndex)
    return custom_range, houses

def all_houses(request):
    # houses = House.objects.all()
    houses, search_query = searchHouses(request)
    custom_range, houses = paginateHouses(request, houses, 10)
    context = {'houses': houses, 'search_query': search_query, 'custom_range': custom_range}
    context = {'houses': houses,}

    return render(request, 'houses.html', context)

def house(request, pk):
    house = House.objects.get(id=pk)
    house_images = house.images.all
    # for image in house_images:
    #     print(image.url)
    if request.method == 'POST':
        payment_type = request.POST['payment_type']
        paid = request.POST['paid']
        

        if int(paid) < house.total_price:
            pay_status = PaymentStatus.objects.filter(payment_status='On instalment').first()
        elif int(paid) == house.total_price:
            pay_status = PaymentStatus.objects.filter(payment_status='paid').first()
        else:
            pay_status = PaymentStatus.objects.filter(payment_status='Unpaid').first()


        if int(paid) < house.total_price:
            payment_type = PaymentType.objects.filter(payment_type='Instalmental').first()
        elif int(paid) == house.total_price:
            payment_type = PaymentType.objects.filter(payment_status='Full payment').first()
        
        Booking.objects.create(
            house = House.objects.get(id=pk),
            payment_type = payment_type,
            pay_status = pay_status,
            paid = paid
        )

    context = {'house': house, 'images': house_images}

    return render(request, 'house.html', context)


def book_house(request, pk):
    house = House.objects.get(id=pk)
    if request.method == 'POST':
        payment_type = request.POST['payment_type']
        paid = request.POST['paid']
        

        if int(paid) < house.total_price:
            pay_status = PaymentStatus.objects.filter(payment_status='On instalment').first()
        elif int(paid) == house.total_price:
            pay_status = PaymentStatus.objects.filter(payment_status='paid').first()
        else:
            pay_status = PaymentStatus.objects.filter(payment_status='Unpaid').first()


        if int(paid) < house.total_price:
            payment_type = PaymentType.objects.filter(payment_type='Instalmental').first()
        elif int(paid) == house.total_price:
            payment_type = PaymentType.objects.filter(payment_type='Full payment').first()
        
        Booking.objects.create(
            house = house,
            payment_type = payment_type,
            pay_status = pay_status,
            paid = paid
        )


def searchBooking(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # tags = Tags.objects.filter(name__icontains=search_query)

    booking = Booking.objects.distinct().filter(
        Q(pay_status__payment_status__icontains=search_query) |
        Q(paid__icontains=search_query) |
        Q(payment_type__payment_type__icontains=search_query) |
        Q(order_time__icontains=search_query)
        # Q(house__conpletion_status__icontains=search_query)
    )

    return booking, search_query

def paginateBooking(request, booking, results):
    pageb = request.GET.get('page')
    # results = 3
    paginatorb = Paginator(booking, results)

    try:
        booking = paginatorb.page(pageb)
    except PageNotAnInteger:
        pageb = 1
        booking = paginatorb.page(pageb)
    except EmptyPage:
        pageb = paginatorb.num_pages
        booking = paginatorb.page(pageb)
    except:
        pageb = 1
        booking = paginatorb.page(pageb)
    leftIndex = (int(pageb) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex =(int(pageb) + 5)

    if rightIndex > paginatorb.num_pages:
        rightIndex = paginatorb.num_pages + 1

    custom_rangeb = range(leftIndex, rightIndex)
    return custom_rangeb, booking


def booking(request):
    booking, search_query = searchBooking(request)
    custom_rangeb, booking = paginateBooking(request, booking, 10)
    context = {'booking': booking, 'search_query': search_query, 'custom_range': custom_rangeb}
    # context = {'booking': booking, 'search_query': search_query,} #'search_query': search_query, 'custom_rangeb': custom_rangeb

    return render(request, 'booking.html', context)

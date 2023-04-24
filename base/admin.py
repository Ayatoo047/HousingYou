from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Booking)
admin.site.register(House)
admin.site.register(HouseImages)
admin.site.register(HouseLocation)
admin.site.register(ConpletionStatus)
admin.site.register(HouseTypes)
admin.site.register(OrderStatus)
admin.site.register(PaymentStatus)
admin.site.register(PaymentType)
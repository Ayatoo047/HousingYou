from django.db import models


class Booking(models.Model):
    house = models.ForeignKey('House', models.CASCADE)# Field name made lowercase.
    payment_type = models.ForeignKey('PaymentType', models.CASCADE, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    pay_status = models.ForeignKey('PaymentStatus', models.CASCADE)
    paid = models.IntegerField(blank=True, null=True)
    house_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)



class ConpletionStatus(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.title


class HouseImages(models.Model):
    house = models.ForeignKey("House", on_delete=models.CASCADE, null=True, related_name='images')
    images = models.ImageField(null=True, blank=True)


class House(models.Model):
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey('HouseTypes', models.CASCADE)  # Field name made lowercase.
    location = models.ForeignKey('HouseLocation', models.CASCADE)  # Field name made lowercase.
    conpletion_status = models.ForeignKey(ConpletionStatus, models.CASCADE,)  # Field name made lowercase.
    # images = models.ForeignKey(HouseImages, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        value = self.location.value
        price = self.type.price

        return (value * price) + price
    
    

class HouseLocation(models.Model):
    location = models.CharField(max_length=45)
    value = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return self.location
    
class HouseOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount_paid = models.IntegerField()
    payment_status = models.ForeignKey('PaymentStatus', models.CASCADE)
    order_status = models.ForeignKey('OrderStatus', models.CASCADE)

    def __str__(self):
        return self.order_status


class HouseTypes(models.Model):
    house_type = models.CharField(max_length=45)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.house_type

class OrderStatus(models.Model):
    order_status = models.CharField(max_length=25)

    def __str__(self):
        return self.order_status
    

class PaymentStatus(models.Model):
    payment_status = models.CharField(max_length=25)

    def __str__(self):
        return self.payment_status


class PaymentType(models.Model):
    payment_type = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.payment_type
    


# class User(models.Model):
#     iduser = models.AutoField(primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'user'

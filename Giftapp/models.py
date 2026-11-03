from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_pics')
    date_joined = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name

    def ProfileImage(self):
        return mark_safe('<img src = {} width="100px">'.format(self.profile_image.url))

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    def __str__(self):
        return self.country_name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)
    def __str__(self):
        return self.state_name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    def __str__(self):
        return self.city_name

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    phone_number = models.IntegerField()
    address = models.TextField()
    image = models.ImageField(upload_to='profile_pics')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return self.address

    def UserImage(self):
        return mark_safe('<img src = {} width="100px">'.format(self.image.url))

class GiftCategory(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='gifts_pics')
    def __str__(self):
        return self.category_name
    def CategoryImage(self):
        return mark_safe('<img src = {} width="100px">'.format(self.image.url))

class GiftItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(GiftCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='gifts_pics')
    brand = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name
    def GiftImage(self):
        return mark_safe('<img src = {} width="100px">'.format(self.image.url))

class ProductCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(GiftItem, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    order_id = models.IntegerField()
    order_status = models.CharField(max_length=100,choices=[("pending","Pending"),("completed","Completed"),("failed","Failed")])

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(GiftItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    shipping_address = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=[("pending","Pending"),("shipped","Shipped"),("delivered","Delivered")])


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=100,choices=[("credit_card","Credit Card"),("debit_card","Debit_Card"),("paypal","PayPal"),("other","Other")])
    status = models.CharField(max_length=100,choices=[("pending","Pending"),("completed","Completed"),("failed","Failed")])
    payment_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.order

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(GiftItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(GiftItem, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now=True)

class ContactUs(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','profile_image','ProfileImage','date_joined')
    list_filter = ('date_joined',)
    search_fields = ('first_name','last_name')
    list_display_links = ('first_name','last_name')
    list_per_page = 2

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('country','state_name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('state','city_name')
    list_filter = ('state','city_name')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','dob','phone_number','address','image','UserImage','country','state','city')
    list_filter = ('state','city')

@admin.register(GiftCategory)
class GiftCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','description','image','CategoryImage')
    list_filter = ('category_name',)
    list_per_page = 2

@admin.register(GiftItem)
class GiftItemAdmin(admin.ModelAdmin):
    list_display = ('user','category','product_name','description','price','stock','image','GiftImage','brand','created_at')
    list_filter = ('category__category_name',)
    list_editable = ('stock',)
    list_per_page = 2
    list_editable_fields = ('product_name',)

@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('user','product','price','quantity','order_id','order_status')
    list_filter = ('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity','total_price','shipping_address','order_date','delivery_date','status')
    list_filter = ('status',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','order','amount','payment_method','status','payment_date')
    list_filter = ('status',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user','product','created_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','product','rating','comment','review_date')
    list_filter = ('rating',)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','phone','created_at')
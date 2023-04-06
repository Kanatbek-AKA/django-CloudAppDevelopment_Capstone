from django.contrib import admin
# from .models import CarDealer, CarMake, CarModel, DealerReview, TuningModel

# Course
# admin.site.register(CarModel, CarModelAdmin)


# Apart
# # CarModelInline class
# class CarModelInline(admin.StackedInline):
#     model = CarModel
#     # fk_name= 'car_make'

# class CarMakeInline(admin.StackedInline):
#     model = CarMake

# class CarDealerInline(admin.StackedInline):
#     model = CarDealer

# class ReviewInline(admin.StackedInline):
#     model = DealerReview

# class TuningInline(admin.StackedInline):
#     model = TuningModel


# # CarModelAdmin class
# class CarModelAdmin(admin.ModelAdmin):
#     model = CarModelInline
#     list_display = ['name', "type"]
#     list_filter = ['type']
#     search_fields = ['name', 'description']

# # CarMakeAdmin class with CarModelInline
# class CarMakeAdmin(admin.ModelAdmin):
#     inlines = [CarModelInline]
#     list_display = ['name']


# # Register models here
# admin.site.register(CarModel, CarModelAdmin)
# admin.site.register(CarMake, CarMakeAdmin)
# admin.site.register(CarDealer)
# admin.site.register(DealerReview)
# admin.site.register(TuningModel)

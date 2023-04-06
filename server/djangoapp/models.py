from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import uuid

# Course
# class CarMake(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, default="AKA motors")
#     description = models.CharField(max_length=1000)

#     def __str__(self) -> str:
#         return self.name


# class CarModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.ForeignKey(CarMake, on_delete=models.CASCADE)
#     type = models.CharField(null=False, max_length=20, )
#     make = models.CharField(null=False, max_length=150, )
#     year = models.DateField(default=now)

#     def __str__(self):
#         return str(self.id)


# class CarDealer:
#     def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
#         self.address = address
#         self.city = city
#         self.full_name = full_name
#         self.id = id
#         self.lat = lat
#         self.long = long
#         self.short_name = short_name
#         self.st = st
#         self.zip = zip

#     def __str__(self):
#         return "Dealer name: " + self.full_name


# This part is apart with additional models.
# class CarMake(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, default="AKA motors")
#     description = models.CharField(max_length=1000)
#     # Choose a continent
#     ASIA = 'Asia'
#     AMERICA = 'America'
#     AFRICA = 'Africa'
#     AUSTRALIA = 'Australia'
#     EUROPE = 'Europe'
#     CONTINENTAL_CAR_BRAND = [
#         (ASIA, 'Asia'),
#         (AMERICA, 'America'),
#         (AFRICA, 'Africa'),
#         (AUSTRALIA, 'Australia'),
#         (EUROPE, 'Europe'),
#     ]
#     car_make = models.CharField(
#         max_length=50, choices=CONTINENTAL_CAR_BRAND, blank=True, default='ASIA')

#     def __str__(self) -> str:
#         return self.name


# class CarModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     # CharField(max_length=50)
#     name = models.ForeignKey(CarMake, on_delete=models.CASCADE)
#     type = models.CharField(null=False, max_length=20, )
#     make = models.CharField(null=False, max_length=150, )
#     year = models.DateField(default=now)

#     def __str__(self):
#         return str(self.id)


# class TuningModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     car_make = models.ForeignKey(
#         CarMake, on_delete=models.CASCADE, related_name='car_made_in')
#     # Car manufacture by continents
#     ASIA = 'Asia'
#     AMERICA = 'America'
#     AFRICA = 'Africa'
#     AUSTRALIA = 'Australia'
#     EUROPE = 'Europe'
#     CAR_TYPE = [
#         (AUSTRALIA, (
#             ('au', "No car manufactures"),
#         )),

#         (ASIA, (
#             ('in', 'Maruti SUZUKI'),
#             ('jp', 'Lexus'),
#             ('cn', 'FAW'),
#             ('jp', 'Acura'),
#             ('jp', 'Subaru'),
#             ('kr', 'Hyundai'),
#             ('ru', "Zhiguli"),
#             ('iran', 'Safari'),
#             ('jp', "Mitsibushi"),
#             ('jp', 'Honda'),
#             ('jp', 'Toyota'),
#             ('jp', ''),
#         )),
#         (AMERICA, (
#             ('mi', "Cadillac"),
#             ('mi', 'Chevrolet'),
#             ('mi', 'Jeep'),
#             ('tx', 'Tesla'),
#             ('mi', 'Lincoln'),
#             ('mi', 'Buick'),
#             ('ca', "Rivian"),
#             ('ca', 'Lucid'),
#             ('mi', 'GMC'),
#             ('mi', 'Pontiac'),
#         )),
#         (AFRICA, (
#             ('ng', 'Innoson IVM G5'),
#             ('gh', 'Kantanka'),
#             ('ug', 'Kiira KMC'),
#             ('ke', 'Mobius'),
#             ('mar', 'Laraki'),
#             ('sa', 'Birkin'),
#             ('sa', 'Optimal'),
#             ('sa', 'Bailey')
#         )),
#         (EUROPE, (
#             ('deu', 'VW'),
#             ('it', 'Stellantis'),
#             ('deu', 'Mercedes-Benz'),
#             ('fr', 'Renault'),
#             ('fr', 'Peigeot'),
#             ('it', 'Fiat'),
#             ('deu', 'BMW'),
#             ('se', 'Volvo'),
#             ('deu', 'Audi'),
#             ('uk', 'Lotus'),
#         )),
#     ]
#     car_type = models.CharField(
#         max_length=50, choices=CAR_TYPE, blank=True, default='Choose continent')

#     # Car tuning
#     STEREO = 'Audio'
#     INTERIOR = 'Salon'
#     MOTOR = 'Engine'
#     SUSPENSION = 'Balance'
#     BODY = 'Aerodynamic'
#     TIRES = 'Tires'
#     COLOR = 'Color'
#     AUTO_STEREO = [
#         (STEREO, (
#             ("select", 'Choose stereo...'),
#             ('sony', 'Wireless XAV-9500ES'),
#             ('piooner', 'DVD AVH-1300NEX'),
#             ('pioneer', 'DMH-C5500NEX'),
#             ('boss', 'BV9358B'),
#             ('atoto', 'A6PF Double-DIN'),
#             ('sony', 'MEX-N4200BT'),
#             ('jvc', 'KWR930BT'),
#             ('kenwood', 'Single DIN'),
#             ('alpine', 'UTE-200BT')
#         ))
#     ]
#     stereo = models.CharField(
#         max_length=100, choices=AUTO_STEREO, blank=True, default='select')

#     AUTO_INTERIOR = [
#         (INTERIOR, (
#             ('a', 'Perfect shine'),
#             ('b', 'Cracks & Crevices'),
#             ('c', 'All in Detail'),
#             ('d', 'Atomic Detail'),
#             ('e', 'Auto Beauty'),
#             ('f', 'Doctor'),
#         ))
#     ]
#     interior = models.CharField(
#         max_length=100, choices=AUTO_INTERIOR, blank=True, default='a')

#     AUTO_ENGINE = [
#         (MOTOR, (
#             ('ford', 'FORD V8 Predator'),
#             ('ram', 'RAM Inline-Six Turbocharged'),
#             ('mazda', 'Mazda SkyActiv-G'),
#             ('ford', 'Ford Twin-Trubo V6'),
#             ('vw', 'VW Twin-Turbo4 V8'),
#             ('chvr', 'Chevrolet V8'),
#             ('dodge', 'Dodge Supercharged V8'),
#             ('ferrari', 'Ferrari Twin-Turbocharged V8'),
#             ('bmw', 'BMW Twin-Trubo V8'),
#             ('audi', 'AUDI Turbocharged Inline Fice')
#         ))
#     ]
#     engine = models.CharField(
#         max_length=100, choices=AUTO_ENGINE, blank=True, default='ford')

#     AUTO_BALANCE = [
#         (SUSPENSION, (
#             ('a', 'Tru-Sin prop'),
#             ('b', 'Ease-Home'),
#             ('c', 'Daytona'),
#             ('d', 'AW3D 8'),
#         ))
#     ]
#     balance = models.CharField(
#         max_length=100, choices=AUTO_BALANCE, blank=True, default='a')

#     AUTO_BODY = [
#         (BODY, (
#             ('a', 'Hatchback'),
#             ('b', 'Sedan'),
#             ('c', 'MUV/SUV'),
#             ('d', 'Copue'),
#             ('e', 'Convertible'),
#             ('f', 'Wagon'),
#             ('g', 'Van'),
#             ('h', 'Jeep'),
#         ))
#     ]
#     body = models.CharField(
#         max_length=100, choices=AUTO_BODY, blank=True, default='a')

#     AUTO_TIRE = [
#         (TIRES, (
#             ('a', 'BFGoodrich'),
#             ('b', 'Bridgestone'),
#             ('c', 'Continental'),
#             ('d', 'Dunlop'),
#             ('e', 'Firestone'),
#             ('f', 'General Tire'),
#             ('g', 'Goodyear'),
#             ("h", 'Hankook'),
#             ('aka', 'Airless'),
#             ('aka', 'Gel'),
#             ('aka', 'Automatic pump'),
#         ))
#     ]
#     tires = models.CharField(
#         max_length=100, choices=AUTO_TIRE, blank=True,  default='a')

#     AUTO_COLOR = [
#         (COLOR, (
#             ('a', 'Long Beach Blue'),
#             ('b', 'Arrow Gray'),
#             ('c', 'Purple Sector'),
#             ('d', 'Mint Green'),
#             ('e', 'Thundernight Metallic'),
#             ('f', 'Electric Blue'),
#             ('g', 'Amplify Orange'),
#             ('h', 'Stryker Red'),
#         ))
#     ]
#     color = models.CharField(
#         max_length=100, choices=AUTO_COLOR, blank=True, default='a')

#     def __str__(self):
#         return self.car_type


# class CarDealer(models.Model):
#     id = models.AutoField(primary_key=True)
#     dealer_id = models.ForeignKey(
#         CarModel, on_delete=models.CASCADE, to_field='id')
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=15)
#     st = models.CharField(max_length=5)
#     address = models.CharField(max_length=50)
#     zip_code = models.CharField(max_length=15)
#     lat = models.FloatField()
#     long = models.FloatField()
#     short_name = models.CharField(max_length=20)
#     full_name = models.CharField(null=False, max_length=50)


# class DealerReview(models.Model):
#         id = models.AutoField(primary_key=True)
#         dealership = models.ForeignKey(
#             CarModel, on_delete=models.CASCADE, to_field="id")
#         car_make = models.CharField(null=False, max_length=50, blank=True)
#         car_model = models.CharField(null=False, max_length=10, blank=True)
#         car_year = models.DateField(null=True, blank=True)
#         name = models.CharField(max_length=100, blank=True)
#         purchase = models.BooleanField(default=False)
#         purchase_date = models.DateField(null=True, blank=True)
#         review = models.TextField()


# # TO fix multiple foreign key, just use for 2,3,4 etc fk_name & related_name='name_of_colum_plus_something'  Done!
# # Not clear if we define name in both car make and model, what name field in car model does do for when the name is already defined by car make. Or car make name is manufacture and car model name of car name with model

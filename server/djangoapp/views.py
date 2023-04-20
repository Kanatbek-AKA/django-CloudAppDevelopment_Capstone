import os
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CarDealer, CarMake, CarModel #DealerReview  
from datetime import datetime
import logging
import json
from django.views.generic import TemplateView
from .restapis import get_dealers, get_reviews, post_reviews, be_aka, analyze_review_sentiments, infoAddress
from datetime import datetime
from requests.exceptions import ConnectionError

import random  # used for dealership in reviews

# from django.core.mail import send_mail, BadHeaderError, EmailMessage
# from .send_grid import send_emails    # used for newsletter weekly, monthly etc 
 

# Get an instance of a logger
logger = logging.getLogger(__name__)


# # Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)


# # Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')


# # Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        # Let's re-work it later to create each differrently
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)


class ErrorPage(TemplateView):
    # model =
    template_name = "djangoapp/error.html"
    # extra_content =


# Update the `get_dealerships` view to render the index page with a list of dealerships
class IndexPageView(TemplateView):
    # model=
    template_name = "djangoapp/index.html"
    extra_context = {"date": datetime.today().strftime("%Y")}

# def get(self, request, **kwargs):
#     context = {}
#     # In case you want to read the stored files in the same folder/ directory
#     # DIRNAME = os.path.dirname(__file__)
#     # file_cld = os.path.join(DIRNAME, 'folder/file.json')
#     # with open(file_cld, mode='r') as temp_js:
#     #     temp_file = json.loads(temp_js.read().strip())
#     if request.method == "GET":
#         return render(request, 'djangoapp/index.html', context)

#     return HttpResponse("Your temp Error file")


# Create an `about` view to render a static about page
class AboutPageView(TemplateView):
    # model=
    template_name = 'djangoapp/about.html'
    # extra_content =


# Create a `contact` view to return a static contact page
class ContactPageView(TemplateView):
    # model=
    template_name = "djangoapp/contact.html"
    # extra_content =


class HQAKAPageView(TemplateView):
    # model =
    template_name = "djangoapp/hq_contact.html"
    # extra_context = 


# class CustomerServicePageView(TemplateView):
#     # model =
#     template_name = "djangoapp/hq_contact.html"
#     # extra_context = 


# class ADSPageView(TemplateView):
#     # model =
#     template_name = "djangoapp/hq_contact.html"
#     # extra_context = 



def infoDevice():
    from platform import platform, machine, system, processor, node
    dct = {
        "devices": platform()[:10],
        'machines': machine(),
        'processors': processor()[:5],
        'nodes': node(),
        'systems': system(),
    }
    return dct

# Testing automation fill in the address and verification
# For new dealers
class NewDealerMember(TemplateView):
    # model =
    template_name = 'djangoapp/member.html'
    # context_object_name=
    extra_context = {"extract": infoDevice()}
    # login_url=
    # success_url=
    # form_class=

    # def get(self, request):
    #     context = []
    #     if request.method == "GET":
    #         dealers_rec = get_dealers()
    #         for row in dealers_rec['body']['rows']:
    #             ids = row['doc']['_id'] 
    #             context.append(ids)
    #         print("Length: ", len(context) )
    #         return render(request, "djangoapp/member.html", {})
    #     return render(request, "djangoapp/member.html", {})
    #     #

    # To find free providers for automation EU/US/CA/Australian, etc addressess by entering Postal/ZIP, City for verification.
    def post(self, request):
        context = []
        dealers_rec = get_dealers()
        for row in dealers_rec['body']['rows']:
            ids = row['doc']['_id'] 
            context.append(ids)
        # print("What the length: ", len(context) + 1)
        if request.method == "POST":
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            short_name = request.POST['shortname']
            dob = request.POST['dob']     # in case you need to collect DOB of new members. TODO add it in restapi.py and payloads below
            address = request.POST['address']
            zipcode = request.POST['zip']
            # city = request.POST['city']
            # state = request.POST['state']      
            st = request.POST['state']           # country code
            # Using JS or Python to get address lat (to create)
            # latitude = request.POST['latitude']
            # Using JS or Python to get address lat (to create)
            # longitude = request.POST['longitude']
            # required JSON serialization
            image = request.FILES['image'].read()
            # Accessed device
            device = infoDevice()['devices'][:10]
            system = infoDevice()['systems']
            processor = infoDevice()['processors'][:5]
            machine = infoDevice()['machines']

            # Get city, state, lat, long 
            validate_addr = infoAddress(zipcode, st)
            addr_detail = {}
            for i in validate_addr['location']:
                addr_detail = i

            payloads = {
                "ids": f"{len(context)+1}",
                'full_name': f"{first_name} {last_name}",
                "short_name": short_name,
                'address': address,
                'city': addr_detail['city'],
                'state': addr_detail['state'],
                'st': st,
                "zipcode": zipcode,
                'latitude': addr_detail['latitude'],
                'longitude': addr_detail['longitude'],
                'date': f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "image": f"{image}",
                "device": device,
                "system": system,
                "processor": processor,
                "machine": machine,
                }
            be_aka(payloads)
            return redirect("djangoapp:registration") 
        
        return render(request, 'djangoapp/member.html', )


# You ca use it in extra_content
# def dealers_aka():
#     dct = {}
#     templ_file = get_dealers()
#     dct['dealerships'] = templ_file['body']['rows']
#     return dct

# Create a `get_dealer_details` view to render the reviews of a dealer
class DealerPageView(TemplateView):
    # model =
    template_name = 'djangoapp/dealer_details.html'
    # context_object_name=
    # extra_context =  {"test": dealers_aka()}
    # login_url=
    # success_url=
    # form_class=

    def get(self, request, **kwargs):  #
        context = {}
        try:
            templ_file = get_dealers()
            context['dealerships'] = templ_file['body']['rows']    
            return render(request, "djangoapp/dealer_details.html", context)
        except (ConnectionError, ConnectionRefusedError ) as err:
            return render(request, 'djangoapp/error.html', {} )


#
class ReviewsView(TemplateView):
    # model = 
    template_name = 'djangoapp/reviews.html'
    # context_object_name =
    # extra_context = 

    def get(self, request):   # HOW to use review_id in CloudantDB NoSQL 
        context = {}
        try:
            dealer = get_dealers()['body']['rows']
            review = get_reviews()['body']['rows']
            if review is not None or review != "":
                context['reviews'] = review
                for i in context['reviews']:
                    value = i['doc']['review']  
                    # print(value)
                    conv = json.dumps(value)
                    # print(conv)  # str
                    sentiment = analyze_review_sentiments(conv)
                    return render(request, "djangoapp/reviews.html", {"data": context['reviews'], "analyse": sentiment})
    


            return render(request, "djangoapp/reviews.html", {})
        except (ConnectionError, ConnectionRefusedError ) as err:
            return render(request, 'djangoapp/reviews.html', {})




# Create a `add_review` view to submit a review
class AddReviewView(TemplateView):
    # model = 
    template_name = 'djangoapp/add_review.html'
    # extra_content =

    def post(self, request):  # Add id
        context = []
        dealers_rec = get_reviews()
        for row in dealers_rec['body']['rows']:
            ids = row['doc']['_id'] 
            context.append(ids)
        # retrieve inputs
        if request.method == "POST":
            name = request.POST['name']
            car_make = request.POST['ctype']
            car_model = request.POST['cmodel']
            purchase = request.POST['purchase']
            client_purchase = request.POST['purchase']
            car_year = request.POST['year']
            review = request.POST['review']
            # Here or in RestApi exclude bool 
            # if purchase == "" or len(purchase) == 0:
            #     payloads = {
            #         'name': name,
            #         'dealership': f'{random.randrange(1, 100, 15)}',
            #         "review": review,
            #         'car_make': car_make,
            #         'car_model': car_model,
            #         'year': car_year,
            #         'bool': purchase,       # passes an emtpy value to CloudantDb
            #         "client_purchase": f"{client_purchase}",
            #         'date': f"{datetime.now().strftime('%Y-%m-%d')}",
            #     }
            #     post_reviews(payloads)
            #     return redirect("djangoapp:reviews")
            # else:
            payloads = {
                "ids": f"{len(context)+1}",
                'name': name,
                'dealership': f'{random.randrange(1, 50, 3)}',
                "review": review,
                'car_make': car_make,
                'car_model': car_model,
                'year': car_year,
                'bool': purchase,          
                "client_purchase": client_purchase,
                'date': f"{datetime.now().strftime('%Y-%m-%d')}",
            }
            post_reviews(payloads)
            return redirect("djangoapp:reviews")

        return render(request, 'djangoapp/add_review.html', {})





# Course
# def get_dealerships(request):
#     if request.method == "GET":
#         url = "your-cloud-function-domain/dealerships/dealer-get"
#         # Get dealers from the URL
#         dealerships = get_dealers_from_cf(url)
#         # Concat all dealer's short name
#         dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
#         # Return a list of dealer short name
#         return HttpResponse(dealer_names)

# For different site
# def add_review(request, dealer_id):

#     if User.is_authenticated:
#         # sample to
#         review["time"] = datetime.utcnow().isoformat()
#         review["dealership"] = 11
#         review["review"] = "This is a great car dealer"

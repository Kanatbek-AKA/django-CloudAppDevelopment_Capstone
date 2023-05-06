import os
from requests.exceptions import ConnectionError, InvalidURL, MissingSchema
from urllib.error import URLError
from urllib3.exceptions import ConnectTimeoutError, NewConnectionError
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CarMake, CarModel, Dealers, CarReviews, ThreeStepCar  
from datetime import datetime
import logging
import json
from django.views.generic import TemplateView # DetailView,ListView,FormView
from .restapis import get_dealers, get_reviews, post_reviews, be_aka, analyze_review_sentiments
from .actions import get_action_dealers, get_action_reviews
from .zipinfo import infoAddress
from datetime import datetime
import random  # used for dealership in reviews

# from django.core.mail import send_mail, BadHeaderError, EmailMessage  
from django.conf import settings                                             # Used for files outside the django project
from .send_grid import send_emails                                           # subcription

# Filter 
# from django import template
# from django.template.defaultfilters import stringfilter
# from django.utils.html import conditional_escape, mark_safe, escape
from django.db.models import Q

# Cross Site Request Forgery protection
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token


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
    # success_url = 

    # def get(self, request):
    #     context = {}
    #     # In case you want to read a stored json file in the same folder/ directory as restapi.py
    #     # DIRNAME = os.path.dirname(__file__)
    #     # file_cld = os.path.join(DIRNAME, 'folder/file.json')
    #     # with open(file_cld, mode='r') as temp_js:
    #     #     temp_file = json.loads(temp_js.read().strip())
    #     if request.method == "GET":
    #         return render(request, 'djangoapp/index.html', {})

    # @csrf_protect
    def post(self, request, **kwargs):
        if request.method == "POST":
            # Three steps
            state = request.POST['stp3_state']
            city_code = request.POST['stp3_citycode']
            phone = request.POST['stp3_phone']

            threeSteps = ThreeStepCar(state=state, city_code=city_code, phone=phone)
            threeSteps.save()
            return render(request, "djangoapp/index.html", {'success': "Submitted successfully!"})    
        return redirect('djangoapp:index', )

    # # Need TODO 
    # def subcribe(request, **kwargs):
    #     if request.method == POST:
    #         subr = request.POST['subcribe']
    #         send_emails(subr)
    #         return render(request, "djangoapp/index.html", {'success': "Subcription confirmed."})



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


# class HQAKAPageView(TemplateView):
#     # model =
#     template_name = "djangoapp/hq_contact.html"
#     # extra_context = 


# class CustomerServicePageView(TemplateView):
#     # model =
#     template_name = "djangoapp/hq_contact.html"
#     # extra_context = 


# class ADSPageView(TemplateView):
#     # model =
#     template_name = "djangoapp/hq_contact.html"
#     # extra_context = 



# def storeJson(request):
#     # context = {}
#     # for row in get_dealers()['body']['rows']:
#     #     ids = row['doc'] 
#     # Use each column and store it like (name by name or )
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     test = Dealers(**body)
#     test.save()
#     return JsonResponse({"result": "OK"})


def infoDevice():
    try:
        from platform import platform, machine, system, processor, node
        from urllib.request import urlopen
        import re as r
        d = str(urlopen('http://checkip.dyndns.com/').read())
        ipdata = r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
        dct = {
            "ip": ipdata,
            "devices": platform()[:10],
            'machines': machine(),
            'processors': processor()[:5],
            'nodes': node(),
            'systems': system(),
        }
        return dct
    except URLError:
        pass

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


    # To find free providers for automation EU/US/CA/Australian, etc addressess by entering Postal/ZIP, City for verification.
    def post(self, request):
        context = []
        try:
            dealers_rec = get_dealers()['body']['rows']    
            for row in dealers_rec:
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
                st = request.POST['state']                   
                # Using JS or Python to get address lat (to create)
                # latitude = request.POST['latitude']
                # Using JS or Python to get address lat (to create)
                # longitude = request.POST['longitude']
                # required JSON serialization
                image = request.FILES['image'].read()
                # Accessed device
                ipdata = infoDevice()["ip"]
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
                    'st': addr_detail['stateCode2'],
                    "zipcode": zipcode,
                    'latitude': addr_detail['latitude'],
                    'longitude': addr_detail['longitude'],
                    'date': f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                    "image": f"{image}",
                    "ip": ipdata,
                    "device": device,
                    "system": system,
                    "processor": processor,
                    "machine": machine,
                    }    
                be_aka(payloads)
                return render(request, "djangoapp/member.html", {"success": "Submitted successfully!"})
        except TypeError as err:
            warning = "The service is currently not available. Please check later."
            return render(request, 'djangoapp/member.html', {'warning': warning})         
        
        return render(request, 'djangoapp/member.html', )


# You ca use it in extra_content
# def dealers_aka():
#     dct = {}
#     templ_file = get_dealers()
#     dct['dealerships'] = templ_file['body']['rows']
#     return dct

# Create a `get_dealer_details` view to render the reviews of a dealer
class DealerPageView(TemplateView):
    model = CarMake
    template_name = 'djangoapp/dealer_details.html'
    # context_object_name=
    # extra_context =  {"test": dealers_aka()}
    # login_url=
    # success_url=
    # form_class=

    def get(self, request ):  
        context = {}
        # user = self.request.user
        # all_items = Dealers.objects.values().all() 
        try:
            # if user.is_authenticated:
            templ_file = get_dealers()['body']['rows']
            context['dealerships'] = templ_file
    
            # Stored in local model DB
            # Need to TODO --.  If the file with the same values do not store else store new values
            # for i in context['dealerships']:
            #     # obj, created = Dealers.objects.filter(
            #     #     Q(full_name="TestFull") | Q(full_name="TestShort"),
            #     # ).get_or_create(
            #     obj= Dealers(
            #         dealer_id=i['doc']['id'],
            #         full_name=i['doc']['full_name'], 
            #         city=i['doc']['city'], 
            #         st=i['doc']['st'], 
            #         state=i['doc']['state'], 
            #         address=i['doc']['address'], 
            #         zipcode=i['doc']['zip'], 
            #         short_name=i['doc']['short_name'], 
            #         lat=i['doc']['lat'], 
            #         long=i['doc']['long']
            #         # defaults={"full_name": i['doc']['full_name']}
            #     )
            #     obj.save()

            return render(request, "djangoapp/dealer_details.html", context)     
        except (InvalidURL, MissingSchema, TypeError, ConnectionError, ConnectionRefusedError) as err:
            # if your DB connection failed, retrieve the data from enabled url
            # if user.is_authenticated:
            url_file = get_action_dealers() # exception retrieves the data
            if url_file is not None:
                context['dealerships'] = url_file
                return render(request, "djangoapp/dealer_details.html", context)
            else:
                # print("NO internet")
                file_cld = os.path.join(settings.FILES_DIR, 'dealerships.json')
                # if user.is_authenticated:
                with open(file_cld, mode='r') as temp_js:
                    temp_file = json.loads(temp_js.read().strip())['dealerships']
                    return render(request, 'djangoapp/dealer_details.html', {'dealerships': temp_file} )    
        except Exception: 
            return redirect('djangoapp:errors',)
        # # except Other Possible HTTP or API errors:
        #     # return render(request, 'djangoapp/.....html', {} )

    
#
class ReviewsView(TemplateView):
    # model = CarReviews
    template_name = 'djangoapp/reviews.html'
    # context_object_name =
    # extra_context = 

    def get(self, request):   # in process... 
        context = {}
        # user = self.request.user
        try:
            # Render values of NoSQL CloudantDB = CouchDB using APIKeys
            # if user.is_authenticated:
            review = get_reviews()['body']['rows']
            if review is not None:
                context['reviews'] = review
                for i in context['reviews']: 
                    # Sentiment NLU IBM
                    value = i['doc']['review']    # get review column 
                    conv = json.dumps(value)      # to string
                    sentiment = analyze_review_sentiments(conv)
                return render(request, "djangoapp/reviews.html", {"data": context['reviews'], "analyse": sentiment})    
            return render(request, "djangoapp/reviews.html", {})
        except (TypeError, InvalidURL, ConnectionError, ConnectionRefusedError, MissingSchema ) as err:
            # if your APIKey connection failed, retrieve the data from enabled url e.g. ibmcloud - functions- actions
            # if user.is_authenticated:
            url_file = get_action_reviews()
            if url_file is not None:
                context['reviews'] = url_file
                for i in context['reviews']: 
                    # Sentiment NLU IBM
                    value = i['doc']['review']    # get review column 
                    conv = json.dumps(value)      # to string
                    sentiment = analyze_review_sentiments(conv)
                    return render(request, "djangoapp/reviews.html", {"data": context['reviews'], "analyse": sentiment})
            else:
                # If both above failed, than read the dealership.json outside the django project e.g. folder cloudant/data/reviews-full.json
                warning = "Service is not available. Please visit later."
                file_cld = os.path.join(settings.FILES_DIR, 'reviews-full.json')
                with open(file_cld, mode='r') as temp_js:
                    temp_file = json.loads(temp_js.read().strip())
                    context['reviews'] = temp_file['reviews']
                    # if user.is_authenticated:
                    for i in temp_file['reviews']:
                        conv = json.dumps(i['review'])
                        sentiment = analyze_review_sentiments(conv)
                        if sentiment is not None: 
                            return render(request, "djangoapp/reviews.html", {"data": context['reviews'], "analyse": sentiment})
                        
                return render(request, "djangoapp/reviews.html", {"warning": warning})
        except (ConnectionError, NewConnectionError, InvalidURL, MissingSchema) as err:
            # # If both above failed, than read the dealership.json outside the django project e.g. folder cloudant/data/reviews-full.json
            # warning = "Service is not available. Please visit later."
            # file_cld = os.path.join(settings.FILES_DIR, 'reviews-full.json')
            # with open(file_cld, mode='r') as temp_js:
            #     temp_file = json.loads(temp_js.read().strip())
            #     context['reviews'] = temp_file['reviews']
            #     # if user.is_authenticated:
            #     for i in temp_file['reviews']:
            #         conv = json.dumps(i['review'])
            #         sentiment = analyze_review_sentiments(conv)
            #         if sentiment is not None: 
            #             return render(request, "djangoapp/reviews.html", {"data": context['reviews'], "analyse": sentiment})
                    
            # return render(request, "djangoapp/reviews.html", {"warning": warning})
            return redirect("djangoapp:errors", )
        # except Other Possible HTTP or API errors:
        #     return render(request, 'djangoapp/add_review.html', {} )





# Create a `add_review` view to submit a review
class AddReviewView(TemplateView):
    # model = 
    template_name = 'djangoapp/add_review.html'
    # extra_content =

    def post(self, request):  # dealership numbers or name 
        context = []
        try: 
            dealers_rec = get_reviews()
            for row in dealers_rec['body']['rows']:
                ids = row['doc']['_id'] 
                context.append(ids)
        
            if request.method == "POST":
                name = request.POST['name']
                car_make = request.POST['ctype']
                car_model = request.POST['cmodel']
                purchase = request.POST['purchase']
                client_purchase = request.POST['purchase']
                car_year = request.POST['year']
                review = request.POST['review']
     
                payloads = {
                    "ids": f"{len(context)+1}",
                    'name': name,
                    'dealership': f'{random.randrange(1, 50, 3)}',
                    "review": review,
                    'car_make': car_make,
                    'car_model': car_model,
                    'year': car_year,
                    'bool': f"{purchase}",          
                    "client_purchase": f"{client_purchase}",
                    'date': f"{datetime.now().strftime('%Y-%m-%d')}",
                }
                post_reviews(payloads)
                return render(request, "djangoapp/add_review.html", {'success': "Submitted successfully!"})
        except TypeError as err:
            warning = "The service is currently not available. Please check later."
            return render(request, 'djangoapp/add_review.html', {'warning': warning})
       
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

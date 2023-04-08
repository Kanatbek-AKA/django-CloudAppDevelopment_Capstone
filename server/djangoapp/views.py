import os
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import DealerReview, CarDealer, CarMake, CarModel
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.views.generic import TemplateView
from .restapis import get_dealers, get_reviews, post_reviews, be_aka, analyze_review_sentiments #, infoAddress
from datetime import datetime
from requests.exceptions import ConnectionError

# from django.core.mail import send_mail, BadHeaderError, EmailMessage

# Test the debug with logging in Django  --> create it server folder

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

    # Used Send Grid to send emails 
    # def post(self, request, **kwargs):
    #     context = {}
    #     if request.method == "POST":
    #     # TODO create email smtp or send-grid


def infoDevice():
    from platform import platform, machine, system, processor, node
    dct = {
    "devices": platform()[:10],
    'machines': machine(),
    'processors':processor()[:5],
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
    
    # To find free providers for automation EU/US/CA/Australian, etc addressess by entering Postal/ZIP, City for verification.   
    def post(self, request): 
        context = {}
        if request.method == "POST":
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            short_name = request.POST['shortname']
            dob= request.POST['dob']
            address = request.POST['address']
            city = request.POST['city'] 
            state = request.POST['state']
            st = request.POST['st']
            zipcode = request.POST['zip']
            latitude = request.POST['latitude']     # Using JS or Python to get address lat (to create)
            longitude = request.POST['longitude']   # Using JS or Python to get address lat (to create)  
            image = request.FILES['image'].read()   #  required JSON serialization 
            # Accessed device 
            device = infoDevice()['devices'][:10]
            system = infoDevice()['systems']
            processor = infoDevice()['processors'][:5]
            machine = infoDevice()['machines']
            
            payloads = {
                'full_name': f"{first_name} {last_name}",
                "short_name": short_name,
                'address': address,
                'city': city,
                'state': state,
                'st': st,
                "zipcode": zipcode,
                'latitude': latitude,
                'longitude': longitude,
                'date': f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "image": f"{image}",
                "device": device,
                "system": system,
                "processor": processor,
                "machine": machine,                           
            }
            be_aka(payloads)
            return redirect("djangoapp:registration")  # Missing something
        return render(request, 'djangoapp/error.html', )

# Create a `get_dealer_details` view to render the reviews of a dealer
class DealerPageView(TemplateView):
    # model =
    template_name = 'djangoapp/dealer_details.html'
    # context_object_name=
    # extra_context =  here you import from local db if you define model above or new function
    # login_url=
    # success_url=
    # form_class=

    def get(self, request, **kwargs):  #
        context = {}
        # try:
        if request.method == "GET":
            templ_file = get_dealers()
            context['dealerships'] = templ_file['body']['rows']
        return render(request, "djangoapp/dealer_details.html", context)
        # except ConnectionError as conn:
        #     return render(request, 'djangoapp/error.html', )

# Additional to get the point
    # data={'name':request.POST.get("device")}
    #    headers = {'content-type': 'application/json'}
    #    response = requests.post('http://localhost:3000/path', data=json.dumps(data), headers=headers)
    # return render(request, 'mytemplate.html', {'allow_redirect': settings.ALLOW_REDIRECT})


#
# Create a `add_review` view to submit a review
class AddReviewView(TemplateView):
    # model = DealerReview
    template_name = 'djangoapp/add_review.html'
    # extra_content = 
        
    def get(self, request):
        # try:
        context = {}
        if request.method == "GET":
            templ_file = get_reviews()
            context['reviews'] = templ_file['body']['rows']
            for i in context['reviews']:
                value = i['doc']   # dict
                print(value)
                conv = json.dumps(value)
                # print(conv)  # str
            sentiment = analyze_review_sentiments(conv)
            return render(request, "djangoapp/add_review.html", {"data": context['reviews'], "analyse": sentiment}) # 
        # except ConnectionError as conn: 
        #     return render(request, 'djangoapp/error.html', )
        

    ## INFO:  additional  user authentucation to post their reviews, it is up to you.
    def post(self, request):
        context = {}
        # dbname = dct['DBNAME2']
        if request.method == "POST":
            name = request.POST['name']
            car_make = request.POST['ctype']
            car_model = request.POST['cmodel']
            purchase = request.POST['purchase']
            car_year = request.POST['year']
            review = request.POST['review']
            payloads = {
                'name': name,
                "review": review,
                'car_make': car_make,
                'car_model': car_model,
                'year': car_year,
                'bool': purchase,
                'date': f"{datetime.now().strftime('%Y-%m-%d')}",
            }
            post_reviews(payloads)

            return redirect("djangoapp:reviews")  # Missing something
        else:
            render(request, 'djangoapp/add_review.html', context)



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

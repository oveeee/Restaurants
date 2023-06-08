from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from customer.models import *
def home(request):
 return render(request, 'home.html')

def address(request):
 return render(request, 'address.html')

def aboutus(request):
 return render(request, 'aboutus.html')

def ourservice(request):
 return render(request, 'ourservice.html')


def Testmonial(request):
 return render(request,'Testmonial.html')

def order(request):
 return render(request, 'order.html')

def login(request):
 return render(request, 'login.html')

#def singup(request):
 #return render(request, 'singup.html')
class RegistrationView(View):
    def get(self, request): 
        form = RegistrationForm()
        return render(request, 'singup.html',{'form':form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        messages.success(request, 'Congratulations! Registered Succesfully')
        if form.is_valid():
            form.save()
        return render(request, 'singup.html',{'form':form})



def changepass(request):
 return render(request, 'changepass.html')

def profile(request):
 return render(request,'profile.html')

def test(request):
    customer1=Customer(full_name='Ove',number='01605501565',user=User.objects.get(username = 'ove'))

    customer1.save()
    

    # Cuisine1=Cuisine(cuisine_name='kekafood',type='fastfood',description='this is best food')

    
    # Menu1=Menu(food_name='BIBIMBAP',food_price=12,unit='2')

    # OrderItem1=OrderItem(Order='Noodless',Menu='Korean')
    # OrderItem.save()
    
    # payment_type1=Payment(Payment_type='Bkash',Order='Noodless',Customer=' 1')
    
    #Order1=order(date_time='2023-04-12', total_price=2000,arrival_time='12,56,20')
    #Order1.save()
    # time(hour = 0, minute = 0, second = 0)
    return render(request,'home.html')



# Create your views here.

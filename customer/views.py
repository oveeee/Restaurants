from django.shortcuts import render
import customer
from customer.forms import CustomerForm
from customer.models import Customer


# Create your views here.
def customer_views(request):
    
    customer_form = CustomerForm()
    if request.method =='POST':
    
        customer_form=customer_form(request.POST)
        customer_form.save()
    customer_form =CustomerForm()

    contest={
        'customer_form':customer_form
    }

    return render(request,'customer/customer.html',contest)

def customers_views(request):
    
    
    if request.method == 'POST':
    
        full_name = request.POST['full_name']
        number = request.POST['number']
        user = request.POST['user']
        customers_object = customers_object(full_name=full_name, number=number, user=user)
        customers_object.save()
        
    
    return render(request,'customer/customers.html')


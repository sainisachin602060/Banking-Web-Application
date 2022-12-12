from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import customer,history

#Create your views here.
def home(request):
    return render(request,'home.html')
    
def balance(request):
    data=customer.objects.all()
    return render(request,'balance.html',{'data':data})

      
def transaction(request):
    name=request.GET['name']
    data=customer.objects.filter(name=name)
    
    data1=customer.objects.all()
    return render(request,'transaction.html',{'data':data,'data1':data1})
  
  
def pay(request):
    
    # fetch Data from select field1
    select_name=request.POST['select1']
    data=customer.objects.filter(name=select_name)
      
    data1=customer.objects.all()
    for i in data:
        select_amount=i.balance
                
    amount2=select_amount
    
    
     #fetch data from amount filed
    amount=request.POST['amount']
    
    
    #fetch data from select field2
    select_name2=request.POST['select2']
    data2=customer.objects.filter(name=select_name2)
    for j in data2:
        select_amount2=j.balance
        
    amount3=select_amount2  
    
    if(amount2 < int(amount) or amount3 < int(amount)):
        return render(request,'transaction.html',{'ms':"Sufficent Balanace try again !",'data1':data1})
    
    
    
    
    # logic to detected amount from customer
    customer.objects.filter(name=select_name2).update(balance=amount3-int(amount))  
    
    #logic to add amount in other customer
    customer.objects.filter(name=select_name).update(balance=int(amount)+amount2)
    #sucessfull message for transaction
    status="successfull recived!"
    ms="Amount has been detected sucessfull !"  
    #render the all data 
    return render(request,'history.html',{'data':data,'data2':data2,'amount':amount,'status':status,'ms':ms})
   



def history(request):
    
    return render(request,'history.html')
            
        
        
        
        
        
        



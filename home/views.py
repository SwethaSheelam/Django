from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def index(request):
    lucky_number=random.randint(50,999)
    Veggies=["potato 🥔","tomato 🍅","chilly 🌶️","beans 🫛","peas 🫘"]
    cities=[{"name":"Japan","population": "37,036,200","country":"india"},
           {"name":"Tokyo","population": "37,036,200","country":"india"},
           {"name":"Tokyo","population": "37,036,200","country":"india"}
    ]
 
    context={"lucky_number":lucky_number,"Veggies":Veggies,"cities":cities}
    return render(request,'index.html',context)

def about(request):
     return render(request,'about.html')

def contact(request):
      return render(request,'contact.html')
  
def dynamic_url(request,id):
      print(f"This is the Value we got from func-> {id}")
      return render(request,'dynamic_url.html',context={"id":id,"name":"Swetha"})
  
def project(request):
      return render(request,'project.html')
  
  
  
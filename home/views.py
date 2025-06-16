from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def index(request):
    lucky_number=random.randint(50,999)
    Veggies=["potato 🥔","tomato 🍅","chilly 🌶️","beans 🫛","peas 🫘"]
    context={"lucky_number":lucky_number,"Veggies":Veggies}
    return render(request,'index.html',context)

def about(request):
     return render(request,'about.html')

def contact(request):
      return render(request,'contact.html')
  
def dynamic_url(request,id):
      print(f"This is the Value we got from func-> {id}")
      return render(request,'dynamic_url.html',context={"id":id,"name":"Swetha"})
  
  
  
  
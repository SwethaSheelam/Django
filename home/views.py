from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
     return render(request,'about.html')

def contact(request):
      return render(request,'contact.html')
  
def dynamic_url(request,id):
      print(f"This is the Value we got from func-> {id}")
      return render(request,'dynamic_url.html',context={"id":id,"name":"Swetha"})
from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.
def country(request):
  qlcto=Country.objects.all()
  d={'Country':qlcto}
  return render(request,'country.html',context=d)

def insert_into_country(request):
  ctid=input('Enter new ctid: ')
  ctn=input('Enter new ctname: ')
  ncto=Country.objects.get_or_create(ctid=ctid,ctname=ctn)[0]
  ncto.save()
  return HttpResponse(f'New data <b><u>{ctid}, {ctn}</u></b> sccuessfully inserted in country table')

def capital(request):
  qlcpo=Capital.objects.all()
  d={'Capital':qlcpo}
  return render(request,'capital.html',context=d)

def insert_into_capital(request):
  ctn=int(input('Enter ctname: '))
  cto=Country.objects.get(ctid=ctn)
  n=input('Enter new cpname: ')
  pop=int(input('Enter population: '))
  ncpo=Capital.objects.get_or_create(ctid=cto,cpname=n,population=pop)[0]
  ncpo.save()
  return HttpResponse(f'New data <b><u>{ctn}, {n}, {pop}</u></b> sccuessfully inserted in capital table')



def display(request):
  return render(request,"display.html")


def display_post(request):
  return render(request,"display_post.html")
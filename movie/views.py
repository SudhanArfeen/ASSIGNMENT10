from django.shortcuts import render
from django.http import HttpResponse
from . models import Movie, contact, order
from django.shortcuts import render,redirect
import json
# Create your views here.

def home(req):
    return render(req,"home.html")
def List(req):
    Movies = Movie.objects.all()
    print (Movie.objects.all)
    params = {
        "data":Movies
    }
    return render(req,"index.html",params)
def login(req):
    return render(req,"login.html")


def signup(req):
    return render(req,"signup.html")

def contactUs(req):
    return render(req,"contactus.html");



def checkout(req):
    str=req.POST.get("cartJson")
    cart=json.loads(str)
    currentCart=cart

    totalPrice=0
    for id in cart:
        temp=cart[id]
        tempObj=Movie.objects.get(id=id)
        price=tempObj.rent_price
        temp["price"]=price
        totalPrice=totalPrice+price
        currentCart[id] = temp
    params = {
        "totalPrice" : totalPrice,
        "data": currentCart
    }
    return render(req,"checkout.html",params)



def contactSubmit(req):
    email=req.POST.get("email")
    name=req.POST.get("name")
    tel=req.POST.get("phone")
    desc=req.POST.get("desc")
    File=req.POST.get("screenshot")
    newContact=contact(email=email,name=name,desc=desc,phone=tel,screenshot=File)
    newContact.save()
    return HttpResponse("Thank You For your Feedback :)")



def submitcheckout(req):
    if(req.method=="POST"):
        jsonCart= req.POST.get("jsonCart")
        first_name= req.POST.get("first_name")
        last_name= req.POST.get("last_name")
        email= req.POST.get("email")
        address= req.POST.get("address")
        state= req.POST.get("state")
        zip= req.POST.get("zip")
        isSameBillingAddress= req.POST.get("isSameBillingAddress")

        if(isSameBillingAddress=="on"):
            isSameBillingAddress = True
        else:
            isSameBillingAddress = False
        newOrder = order (jsonCart=jsonCart,email=email, first_name=first_name ,last_name=last_name,state=state,zipcode=zip,address=address,isSameBillingAddress=isSameBillingAddress)
        newOrder.save()
        return HttpResponse("Thank you for ordering!!")
    else:
        return HttpResponse("You are on a wrong page. please <a href='/movie/list'>Click here</a> to add items")
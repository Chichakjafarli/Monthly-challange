from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#def January(request):
    #return HttpResponse("Eat no meat for the entire month!")

#def February(request):
   # return HttpResponse("Walk for at least 20 minutes every day!")
'''def March(request):
    return HttpResponse("Learn django for at least 20 minutes every day!")
'''
monthly_challenges1={
    "january":"Eat no meat for the entire month!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn django for at least 20 minutes every day!",
    "april":"Eat no meat for the entire month!",
    "may":"Walk for at least 20 minutes every day!",
    "june":"Learn django for at least 20 minutes every day!",
    "july":"Eat no meat for the entire month!",
    "august":"Walk for at least 20 minutes every day!",
    "september":"Learn django for at least 20 minutes every day!",
    "october":"Eat no meat for the entire month!",
    "november":"Walk for at least 20 minutes every day!",
    "december":"Learn django for at least 20 minutes every day!"
}

def index(request):
    list_items =""
    months=list(monthly_challenges1.keys())
    
    for month in months:
        capitalized_month=month.capitalize()
        month_path=reverse("month-challenge",args=[month])
        list_items += f"<li><h1><a href=\"{month_path}\">{capitalized_month}</a></h1></li>"
    
    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_numbers(request,month):
   months=list(monthly_challenges1.keys())
   if month>len(months):
       return HttpResponseNotFound("Invalid month!")
   redirect_month=months[month-1]
   redirect_path=reverse("month-challenge",args=[redirect_month])
   return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text=monthly_challenges1[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>this month is not support!</h1>")

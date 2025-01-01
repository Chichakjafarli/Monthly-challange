from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string 
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
    "december":None
}

def index(request):
    months = list(monthly_challenges1.keys())
    
    return render(request,"challenges/index.html",{
       "months":months
   })


def monthly_challenges_by_numbers(request,month):
   months=list(monthly_challenges1.keys())
   if month>len(months):
       return HttpResponseNotFound("<h1>Invalid month!<h1>")
   redirect_month=months[month-1]
   redirect_path=reverse("month-challenge",args=[redirect_month])
   return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text=monthly_challenges1[month]
        return render(request,"challenges/challenge.html",
                      {"text":challenge_text,
                      "month_name":month
                       })
    except:
       response_data= render_to_string("404.html")
       return HttpResponseNotFound(response_data)

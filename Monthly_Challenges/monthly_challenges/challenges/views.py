from django.shortcuts import render
from django.http import HttpResponse,Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string





# Create your views here Below.

"""
# def january(request):
#     return HttpResponse("eat no meat for the entire month!")
# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day this month!")
# def march(request):
#     return HttpResponse("Write a new blog post every day this month!")"""

#month is identifier that acts like key word value that conncect to challenges.urls.py
#the monthly_challenges_bynumber assist with make the code more dynamic and prevents
#the need to create a new function for each month like january, february, and march, above.

"""
def monthly_challenge(request,month):
    challenge_text = None
    if month == "january":
        return HttpResponse("eat no meat for the entire month!")
    elif month == "february":
        return HttpResponse("Walk for at least 20 minutes every day this month!")
    elif month == "march":
        return HttpResponse("Write a new blog post every day this month!")
    else:
        return HttpResponseNotFound("This month is not supported!")
"""
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day this month!",
    "march": "Write a new blog post every day this month!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day this month!",
    "june": "Write a new blog post every day this month!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day this month!",
    "september": "Write a new blog post every day this month!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day this month!",
    "december": None,
    


}   

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html",{ #this is the context
        "months":months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # #What it will look like => "<li><a href="/challenge/january">January</a></li>"
    # response_data = f"<ul>{list_items}</ul>"    
    # return HttpResponse(response_data)

def monthly_challenges_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        selected_month = month
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{

            "month":selected_month,
            "text":challenge_text

            })
    except:
        raise Http404()
from django.urls import path
from . import views


"""
#UrlConfig
"""
urlpatterns = [
    path("", views.index, name="index"), #/challenge/

    # path("january",views.january),
    # path("february",views.february),
    # path("march",views.march),

    #converts the month to an integer
    #this path filters by integer
    path("<int:month>", views.monthly_challenges_by_number),

    #the code below is more dynamic and prevents the need to create 
    # a new function for each month like january, february, and march, above.
    #month is identifier that conncect to challenges.views.py
    #converts the month to a string
    #this filter for string
    path("<str:month>", views.monthly_challenge, name="month-challenge"),



]

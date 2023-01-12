from django.shortcuts import render,redirect
import random,requests,json
from .models import countryModel
import pandas as pd

def home(request):
    """ Select random country """
    randomCountry = [i.__dict__['country'] for i in countryModel.objects.all()][random.randrange(0,len(countryModel.objects.all()),1)]

    """ listen for form submit and redirect with answer """
    if request.method == "POST":
        return redirect(f"results/{request.POST['countryQuestion']}/{request.POST['capitalAnswer']}")



    context = {
        "randomCountry":randomCountry,
    }

    return render(request,'home.html',context=context)

def results(request,randomCountry,capitalAnswer):
    if str(capitalAnswer).capitalize() == countryModel.objects.get(country=randomCountry).__dict__['capital']:
        result = True
    else:
        result = False

    context = {
        "capitanAnswer":str(capitalAnswer).capitalize(),
        "randomCountry":randomCountry,
        "result":result,
        "correctCapital":countryModel.objects.get(country=randomCountry).__dict__['capital']
    }

    return render(request,"quiz/quizResults.html",context=context)
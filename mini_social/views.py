
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime

def homePage(request):
    current_year = datetime.datetime.now().year
    return render(request, 'home.html', {
        
        'current_year': current_year
    })


def signinPage(request):
    
    template = loader.get_template('signin.html')
    current_year = datetime.datetime.now().year
    return HttpResponse(template.render( {
        'current_year': current_year
        
    }))

def signupPage(request):
    current_year = datetime.datetime.now().year
    return render(request, 'signup.html', {
       
        'current_year': current_year
    })

def termsH(request):
      current_year = datetime.datetime.now().year
      return render(request, 'terms.html', {
       
        'current_year': current_year
    })

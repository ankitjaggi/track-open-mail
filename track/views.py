from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
def track_mail(request):
    print request
    email = request.GET.get('email')
    print email
    if email:
        print 'Mail opened by '+str(email)
    else:
        print "No email specified"

    return redirect('/static/package.png')


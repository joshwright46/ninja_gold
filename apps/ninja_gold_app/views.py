from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    context = {
        'gold' : request.session['gold'],
        'activities' : request.session['activities'] 
    }

    return render(request, 'ninja_gold_app/ninja_gold.html', context)

def destroy_session(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')

def process_money(request):
    if request.method == "POST": 
        if request.POST['building'] == 'farm':
            winnings = random.randrange(10, 21)
            request.session['gold'] += winnings
            activity = f"<p style='color:green'>Earned {winnings} gold from the {request.POST['building']} at {datetime.datetime.now()}</p>"
            request.session['activities'].insert(0,activity)

        if request.POST['building'] == 'cave':
            winnings = random.randrange(5, 11)
            request.session['gold'] += winnings
            activity = f"<p style='color:green'>Found {winnings} gold in the {request.POST['building']} at {datetime.datetime.now()}</p>"
            request.session['activities'].insert(0,activity)

        if request.POST['building'] == 'house':
            winnings = random.randrange(2, 6)
            request.session['gold'] += winnings
            activity = f"<p style='color:green'>Earned {winnings} gold from the {request.POST['building']} at {datetime.datetime.now()}</p>"
            request.session['activities'].insert(0,activity)

        if request.POST['building'] == 'casino':
            winnings = random.randrange(-50, 51) 
            request.session['gold'] += winnings
            if winnings > 0:
                activity = f"<p style='color:green'>Won {winnings} gold at the {request.POST['building']} at {datetime.datetime.now()}</p>"
            elif winnings < 0:
                activity = f"<p style='color:red'>Lost {abs(winnings)} gold at {request.POST['building']} at {datetime.datetime.now()}</p>"
            request.session['activities'].insert(0,activity)

    return redirect('/')

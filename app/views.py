from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Service,Answers
from django import forms
from django.utils import timezone
from app.forms import FirstForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
import json

def index(request):
    return render(request,"app/index.html")
    
def cntinue(request):
    s = Service.objects.filter(id=5)
    if request.POST:  
		a1 = request.POST.get('val')
    for i in s:
		if a1 =='excellent':
			i.excellent +=1
			i.save()
		if a1 =='good':
			i.good +=1
			i.save()
		if a1 =='average':
			i.average +=1
			i.save()
		if a1 =='worst':
			i.worst +=1
			i.save()
    return HttpResponseRedirect("/ThankYou/")
def nextPage(request):
    return render(request,"app/cntinue.html")

def answers(request):
    return render(request,"app/answers.html")
      

def thankss(request):
    if request.POST and request.is_ajax():  
		a1 = request.POST.get('an1')
		a2 = request.POST.get('an2')
		a3 = request.POST.get('an3')
            	if (a1 == "" or a2 == "" or a3 == "" ):
			return HttpResponse("fail")
		else:
			q = Answers(ans1=a1,ans2 = a2, ans3 = a3)
			q.save()
                        data = {"result":"success"}
        		return HttpResponse(json.dumps(data),content_type='application/json')
    else:
                return render(request,"app/answers.html")
def thanks(request):
    return render(request,"app/thanks.html")    
   

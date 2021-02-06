from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from restrauntapp.forms import SignupForm
from django.http import HttpResponseRedirect
from restrauntapp.models import FoodDetails
from django.db.models import Q
from django.contrib import messages

# Create your views here.

@login_required
def welcome_user(request):
	detail=FoodDetails.objects.all()
	my_dict={'detail':detail}
	return render(request,"restrauntapp/welcome-user.html",context=my_dict)

@login_required
def search(request):
	sr=FoodDetails.objects.all()
	if request.method=="POST":
		srch=request.POST['srh']
		if srch:
			match=FoodDetails.objects.filter(Q(price__contains=srch)|Q(foodname__icontains=srch))
			if match:
				return render(request,'restrauntapp/search.html',{'sr':match})
			else:
				messages.error(request,'no result found')

		else:
			return HttpResponseRedirect('/result/')

	return render(request,'restrauntapp/search.html')
	
@login_required
def result(request):
	return render(request=request,template_name='restrauntapp/result.html')

def home_page_view(request):
	return render(request=request,template_name='restrauntapp/homepage.html')

@login_required
def food_category(request):
	return render(request=request,template_name='restrauntapp/food_category.html')



@login_required
def food_item(request):
	return render(request=request,template_name='restrauntapp/food_item.html')

def logout_page(request):
	return render(request=request,template_name='restrauntapp/logout.html')

def gujrat_food(request):
	return render(request=request,template_name='restrauntapp/gujrat.html')

def panjab_food(request):
	return render(request=request,template_name='restrauntapp/panjab.html')

def tamil_food(request):
	return render(request=request,template_name='restrauntapp/tamil.html')
def bengali_food(request):
	return render(request=request,template_name='restrauntapp/bengali.html')

def rajastani_food(request):
	return render(request=request,template_name='restrauntapp/rajastani.html')

def kar_food(request):
	return render(request=request,template_name='restrauntapp/karnataka.html')

def maharashtra_food(request):
	return render(request=request,template_name='restrauntapp/maharashtra.html')

def kerala_food(request):
	return render(request=request,template_name='restrauntapp/kerala.html')
	

def signup_page(request):
	form=SignupForm()
	my_dict={'form':form}
	if request.method=="POST":
		form=SignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
		return HttpResponseRedirect('/accounts/login/')

	return render(request=request, template_name='restrauntapp/signup.html',context=my_dict)
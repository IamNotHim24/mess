from django.shortcuts import render
from .models import Restaurant
from .forms import resReviewForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.http.response import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request,'index.html')

def rev_list(request):
    reviews = Restaurant.objects.all()
    return render(request, 'rev_list.html',{'rev': reviews})

@login_required
def rev_create(request):
    if request.method == "POST": 
        form = resReviewForm(request.POST,request.FILES)
        if form.is_valid():
            rev = form.save(commit=False)
            rev.user = request.user
            rev.save()
            return redirect('rev_list')
        else:
            return HttpResponse(json.dumps(form.errors))
    else:
        id = request.GET['id']
        restuarant = Restaurant.objects.get(id=id)
        reviews = restuarant.reviews.all()
        form = resReviewForm()
    return render(request,'res_form.html',{'form':form,'restaurant':restuarant,'reviews':reviews})

def rev_edit(request,rev_id):
    rev = get_object_or_404(Restaurant,pk=rev_id, user=request.user)
    if request.method=='POST':
        form = resReviewForm(request.POST,request.FILES,instance=rev)
        if form.is_valid():
            rev = form.save(commit=False)
            rev.user = request.user
            rev.save()
            return redirect('rev_list')
    else:
        form = resReviewForm(instance=rev)
    return render(request,'res_form.html',{'form':form})

def rev_del(request,rev_id):
    rev = get_object_or_404(Restaurant,pk=rev_id, user=request.user)
    if request.method=='POST':
        rev.delete()
        return redirect('rev_list')
    return render(request,'rev_confirm_delete.html',{'rev':rev})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('rev_list.html')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
        
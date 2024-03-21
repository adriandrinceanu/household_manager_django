from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .models import Chore, Family  # Import your models
from .utils import create_chore  # Import the create_chore function



def logoutPage(request):
    logout(request)
    return redirect('/')
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            print("working")
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)
   
def homepage(request):
    return render(request, 'home.html')
   
def create_chore_view(request, family_id):
    # Your view logic to handle creating a chore...
    if request.method == 'POST':
        # Get form data
        title = request.POST['title']
        assigned_to = request.user  # Assuming you get the assigned user from the request
        family = Family.objects.get(pk=family_id)
        # Create the chore object (logic here)
        chore = Chore.objects.create(title=title, assigned_to=assigned_to, family=family)
        create_chore(assigned_to, title, family, chore)  # Call the create_chore function
        # Handle successful creation and potentially redirect
    return render(request, 'create_chore.html')
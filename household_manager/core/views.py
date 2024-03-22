from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login,logout,authenticate
from .models import Chore, Family  
from .utils import create_chore  # Import the create_chore function
from .forms import MemberCreationForm, FamilyMemberForm

def homepage(request):
    return render(request, 'home.html')

def logoutPage(request):
    logout(request)
    return redirect('/')
 
def loginPage(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
        context = {}
        return render(request, 'login.html', context)
    
    
def registerPage(request):
    form=MemberCreationForm()
    fam_form=FamilyMemberForm()
    if request.method=='POST':
        form=MemberCreationForm(request.POST)
        fam_form=FamilyMemberForm(request.POST)
        if form.is_valid() and fam_form.is_valid():
            user=form.save()
            customer=fam_form.save(commit=False)
            customer.user=user 
            customer.save()
            return redirect('/')
    context={
        'form':form,
        'cust_form':fam_form,
    }
    return render(request,'register.html',context)

   
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
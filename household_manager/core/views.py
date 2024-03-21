from django.shortcuts import render
from .models import Chore, Family  # Import your models
from .utils import create_chore  # Import the create_chore function

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
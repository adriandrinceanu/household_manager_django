from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django import forms
from .models import Member, Family, Chore, Budget, Expense

def generate_unique_username_from_str(name):
    # Create the initial username
    name = name.replace(' ', '_')
    username = f"{name}".lower()
    # Ensure the username is unique
    User = get_user_model()
    counter = 0
    while User.objects.filter(username=username).exists():
        counter += 1
        username = f"{name}_{counter}".lower()
    return username

class MemberCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=150, required=True)
    profile_pic = forms.ImageField()
    role = forms.ModelChoiceField(queryset=Group.objects.all())
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=200, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['phone', 'profile_pic', 'role', 'name', 'email'] 

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        username = generate_unique_username_from_str(self.cleaned_data['name'])
        user.username = username
        user.set_password(username)
        user.save()
        user.groups.add(self.cleaned_data['role'])
        member = Member.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            profile_pic=self.cleaned_data['profile_pic']
        )
        if commit:
            member.save()
        return user
        
class FamilyCreationForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name', 'profile_pic']
        
        
        
class ChoreCreationForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = ['title', 'description', 'assigned_to']

class BudgetCreationForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'category']

class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'category', 'created_by']
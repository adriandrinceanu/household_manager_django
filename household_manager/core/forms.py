from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Member, Family, Chore, Budget, Expense

class MemberCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=150, required=True)
    profile_pic = forms.ImageField()

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = UserCreationForm.Meta.fields + ('phone', 'profile_pic',)
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
class FamilyCreationForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name', 'profile_pic']
        
class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'profile_pic']
        
        
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
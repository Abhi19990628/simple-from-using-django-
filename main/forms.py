from django import forms
from .models import person  
from datetime import date
class PersonForm(forms.ModelForm):
    class Meta:
        model = person 
        fields = ['firstname','lastname', 'date_of_birth', 'email', 'phone_number']
        
    
    

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        if (date.today() - dob).days / 365 < 18:
            raise forms.ValidationError("You must be 18 years or older to submit this form.")
        return dob
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) < 10:
            raise forms.ValidationError("Please enter a valid phone number with at least 10 digits.")
        return phone_number

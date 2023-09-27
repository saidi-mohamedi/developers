from django.forms import ModelForm 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm  
from .models import Skill , Message 


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','email','username','password1','password2'] 
        
        labels = {
            'first_name': 'Name',
            'email': 'Email',
        }

class SkillsForm(ModelForm):  
    class Meta:
        model = Skill
        fields = ['name','description']     
        
        
class MessageForm(ModelForm):
    class Meta:
        model = Message 
        fields = ['name','email','subject','body']         
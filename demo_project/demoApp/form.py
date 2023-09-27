from django.forms import ModelForm, widgets  
from .models import Project ,Review
from django import forms 


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','featured_image','demo_link','source_link','tags']
        '''
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        } '''
    
        
       
class ReviewForm(ModelForm):
    class Meta:
        model = Review 
        fields = ['value','body']  
    
        labels = {
        'value':'Place your vote here',
        'body': 'Add a comment with your vote'
            }          
    
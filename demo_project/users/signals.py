from django.db.models.signals import post_save, post_delete 
from django.dispatch import receiver 
from django.contrib.auth.models import User 
from .models import Profile 

from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender,instance,created,**kwarg): 
   if created:
       user = instance 
       profile = Profile.objects.create(
           user=user,
           username=user.username,
           email=user.email,
           name = user.first_name, 
       ) 
       
    
       subject = 'Welcome to demoApp project'
       message = 'eddie-gwahisa ndio mwahisa Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula,'

       send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
   
       
     
def deleteUser(sender,instance, **kwargs):
   try:
    user = instance.user 
    user.delete()
   except:
      pass      
    
    
post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser, sender=Profile)    
 
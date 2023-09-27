from django.urls import path
from . import views 
urlpatterns = [ 
    path('', views.home , name = 'home'),           
    path('login/', views.loginUser, name = 'login'),   
    path('userLogout/', views.logoutUser, name='user-logout'),  
    path('register/', views.registerUser, name ='register'),       
    path('profile/', views.profile, name='profile'),
    path('detail-profile/<str:pk>/', views.detailProfile, name='detail-profile'),
    path('user-account', views.userAccount, name='user-account'),
    path('create-skills', views.createSkills, name='create-skills'),
    path('update-skills/<str:pk>/', views.updateSkills, name='update-skills'),
    path('delete-skills/<str:pk>/', views.deleteSkills, name='delete-skills'),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/',views.viewMessage, name="message"),
    path('create-message/<str:pk>/',views.createMessage, name="create-message"),
]
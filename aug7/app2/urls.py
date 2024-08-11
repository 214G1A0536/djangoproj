from django.urls import path
from app2 import views 


urlpatterns=[
    path('',views.func1,name="HomePage"),
    path('login',views.func2,name="LoginPage"),
    path('profile',views.func4,name="ProfilePage"),
    path('logout',views.func4,name="LogoutPage"),
    path('register',views.func5,name="RegisterPage"),
    path('create',views.func7,name="TweetPage"),
    #path('create',views.tweetView,name='createpost'),
    #path('delete/<int:rid>',views.deleteView,name='deletepost'),
    #path('display/<int:rid>',views.display,name='showPost'),
]
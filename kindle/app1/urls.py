from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.home,name="homePage"),
    path('a',views.createAuthor,name="author"),
    path('b',views.createBook,name="book")
]

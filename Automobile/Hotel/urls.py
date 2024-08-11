from django.urls import path
from Hotel import views
urlpatterns=[
    path('app',views.home),
    path('wish',views.add)
]
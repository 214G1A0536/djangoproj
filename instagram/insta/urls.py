from django.urls import path
from insta import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.func1,name='homepage'),
    path('feed',views.func2,name='feedpage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
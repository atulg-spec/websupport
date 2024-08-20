from django.urls import path
from home.views import *
# urls.py
urlpatterns = [
    path("",index,name='index'),
    path('upload_csv/', upload_csv, name='upload_csv'),
    path('<slug:slug>',watch, name='watch'),
    path("about",about,name='about'),
    path("disclaimer",disclaimer,name='disclaimer'),
    path("termsofuse",termsofuse,name='termsofuse'),
    path("privacypolicy",privacypolicy,name='privacypolicy'),
    path("refundpolicy",refundpolicy,name='refundpolicy'),
]

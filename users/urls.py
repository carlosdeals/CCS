# users/urls.py

from django.conf.urls import url
from users.views import dashboard, register


urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    

    
]

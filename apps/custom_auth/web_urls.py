from django.urls import path
from . import views

app_name = 'custom_auth__web'

urlpatterns = [
    path("",views.docker_try,name="docker_try")
]
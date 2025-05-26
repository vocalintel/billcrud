from django.urls import path,include
from django.conf import settings
from .views import *
from billboard import views
from django.urls import path
from django.contrib.auth.views import LoginView
from rest_framework import routers
from . import views
# Create your tests here

router=routers.DefaultRouter()
router.register(r'contacts',views.ContactViewSet)
app_name="billboard"

urlpatterns=urlpatterns = [
    path("billboard",index,name="billboards"),
    path("registration",Registration, name="registration"),
    path("dashboard/<str:user_username>",Dashboard, name="dashboard"),
    path("gateway",Gate,name="gateway"),
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]




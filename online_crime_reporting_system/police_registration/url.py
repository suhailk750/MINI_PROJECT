from django.conf.urls import url
from police_registration import views

urlpatterns = [
    url('police_reg/',views.preg),
    url('mngpolice/',views.mpolice),
    url('apr/(?P<idd>\w+)',views.approve),
    url('rjt/(?P<idd>\w+)',views.reject),

]
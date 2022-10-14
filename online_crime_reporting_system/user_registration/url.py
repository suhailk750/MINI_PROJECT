from django.conf.urls import url
from user_registration import views

urlpatterns = [
    url('user_reg/',views.ureg),

]
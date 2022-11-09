from django.conf.urls import url

from criminal_list import views

urlpatterns = [

   url('crl_post/',views.crlp),
   url('crl_police/',views.crlistp),
   url('crl_view/',views.crlview)




]
from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('cmp_post/',views.cmp),
    url('cmp_view',views.cmpview),
    url('rjt/(?P<idd>\w+)',views.reject),

]
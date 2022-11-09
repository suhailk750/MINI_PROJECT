from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('cmp_post/',views.cmp),
    url('cmp_view',views.cmpview),
    url('view_response/',views.viwresponse),
    url('post_res/(?P<idd>\w+)',views.response,name="rs"),
    url('rjt/(?P<idd>\w+)',views.reject),
    url('vw_em/', views.vem),

]
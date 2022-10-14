from django.conf.urls import url

from temp import views
urlpatterns=[
    url('admint/',views.admin),
    url('homet/',views.home),
    url('usert/',views.user),
    url('policet/',views.police)
]

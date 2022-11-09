from django.conf.urls import url

from emergency_number import views

urlpatterns = [
    url('emnump/', views.emnump),
    url('enuplc/',views.emnumpolice),
    url('emnum_view/',views.emnumview)

]
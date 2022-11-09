from django.conf.urls import url
from missing_person import views

urlpatterns = [
    url('post/',views.mipep),
    url('mpolice/',views.mipepolice),
    url('mipe_view/',views.mipeview)

]
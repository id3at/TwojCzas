from django.urls import include, path
from czas.views import KontaktModelView, sukces, get_name2
urlpatterns = [

    path('kontakt/', KontaktModelView.as_view()),
    path('sukces/', sukces,),
    path('', get_name2,),



]

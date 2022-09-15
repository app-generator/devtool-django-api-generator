from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from apps.api.views import BookView, PersonView, CityView

urlpatterns = [

	re_path("books/((?P<pk>\d+)/)?", csrf_exempt(BookView.as_view())),
	re_path("people/((?P<pk>\d+)/)?", csrf_exempt(PersonView.as_view())),
	re_path("cities/((?P<pk>\d+)/)?", csrf_exempt(CityView.as_view())),

]
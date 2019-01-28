from django.conf.urls import url, include

from pins.views import PinView

urlpatterns = [
    url(r'pins/(?P<pin>\d*)', PinView.as_view()),
]
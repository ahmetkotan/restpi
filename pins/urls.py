from django.conf.urls import url, include

from pins.views import PinView, PinIndexView

urlpatterns = [
    url(r'^$', PinIndexView.as_view()),
    url(r'^api/(?P<pin>\d*)', PinView.as_view()),
]
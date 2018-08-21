from django.conf.urls import url

from .views import RegistrationAPIView, LoginAPIView, UserRetrievUpdateAPIView

urlpatterns = [
    url(r'^user/?$', UserRetrievUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]

from django.urls import path

from weatherapi.views import indexView, resultView
# app_name = 'res'

urlpatterns = [
    path("", indexView, name="home"),
    path("result", resultView, name="result"),
]

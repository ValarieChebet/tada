#from django.conf.urls import url # type: ignore
from django.urls import path # type: ignore
from .views import (
    TadaListApiView,
)

urlpatterns = [
    path('api', TadaListApiView.as_view()),
]
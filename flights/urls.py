from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.FlightsViewSet, basename='flights')


urlpatterns = [
    path('', views.FlightsViewSet.as_view(), name='flights'),
]
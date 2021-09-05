from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.FlightsViewSet, basename='flights')


urlpatterns = [
    path('find_flight/', views.FlightSearchView.as_view(), name='find_flight'),
    path('', include(router.urls)),

]
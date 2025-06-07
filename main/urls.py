from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('component/',views.component_view,name='component'),
    path('details/',views.details_view,name='details'),
]
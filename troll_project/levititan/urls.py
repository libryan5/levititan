from django.urls import path
from levititan.views import liga, levititan

urlpatterns = [
    path('test/', liga),
    path('', levititan)
]

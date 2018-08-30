from django.urls import path
from .views import get_dates, show_data
urlpatterns = [
    path('', get_dates, name='dates'),
    path('show/<slug:date1>&<slug:date2>/', show_data, name='show')
]

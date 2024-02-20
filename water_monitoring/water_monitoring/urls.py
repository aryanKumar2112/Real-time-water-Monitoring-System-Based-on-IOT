from django.contrib import admin
from django.urls import path
from iotData.views import iotDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/iotData/', iotDataView.as_view()),
]


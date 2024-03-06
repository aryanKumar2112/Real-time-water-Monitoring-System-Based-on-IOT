from django.contrib import admin
from django.urls import path, include
from iotData.views import iotDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/iotData/', iotDataView.as_view()),
    path('', include('iotData.urls'))
]


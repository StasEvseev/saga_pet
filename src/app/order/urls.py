from django.urls import re_path, path
from .views import place_order_view

app_name = "order"

urlpatterns = [
    path('place/<customer_id>/<amount>', place_order_view, name='place_order'),
]

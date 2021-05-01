# Django Library
from django.urls import path


# Local Library
from .views import DriverDetailsAPI,RideDetailsAPI

urlpatterns = [
    path('driver/new/', DriverDetailsAPI.as_view(), name='driver-api'),
    path('driver/<int:driver_id>/rides/', RideDetailsAPI.as_view(), name ='driver_ride_detauls')
    # path('shippinglocations/', ShippingLocationAPI.as_view(), name='shippinglocations'),
    # path(
    #     'shippinglocations/<int:shipping_location>/logistic-partners/',
    #     LogisticPartnerShippingLocationLinkAPI.as_view(), name='shippinglocations-logistic-partners-link'),
    # path(
    #     'warehouses/<int:warehouse_id>/logistic-partners/',
    #     LogisticPartnerLinkAPI.as_view(), name='warehouses-logistic-partners-link'),
]

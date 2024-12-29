from django.urls import path
from .views import add_donation_types,add_donation,donation_type_page_view,donation_page_view


urlpatterns = [
    path('add-donation-types/',add_donation_types,name='add_donation_types'),
    path('add-donation/',add_donation,name='add_donation'),
    path('donation/',donation_type_page_view,name='donations_types'),
    path('donation/<int:id>',donation_page_view,name='donations')
    
]

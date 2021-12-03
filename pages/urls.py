from django.urls import path
from .views import error_page, checkout, faq, privacy_policy, return_policy, terms_conditions

app_name = 'pages'

urlpatterns = [
    path('404/', error_page, name='404'),
    path('checkout/', checkout, name='checkout'),
    path('faq/', faq, name='faq'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('return_policy/', return_policy, name='return_policy'),
    path('terms_conditions/', terms_conditions, name='terms_conditions'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.sign_in,name='login'),
    path('add_product/',views.add_product,name='add_product'),
    path('get_products/',views.get_products,name='get_products')
]
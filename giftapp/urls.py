from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('login/',views.login,name='login'),
    path('regist/',views.registration,name='registration'),
    path('upload_image/',views.upload_image,name='upload_image'),
    path('logout/',views.logout,name='logout'),
    path('add_to_cart/<int:pk>/', views.add_to_cart,name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart,name='remove_from_cart')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
URL configuration for EShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from products.views import (HomePage, main_page, ShopPage, detail_page, cart_page, contact_page,
                            logout_view, MyLoginView, search, category_page, user_cart, add_products_to_user_cart,
                            delete_user_cart, RegisterUser)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('index', main_page, name='index'),
    path('shop', ShopPage.as_view(), name='shop'),
    path('detail/<int:pk>', detail_page, name='detail'),
    path('cart', cart_page, name='cart'),
    path('contact', contact_page, name='contact'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('search', search),
    path('category/<int:pk>', category_page),
    path('user_cart', user_cart, name='cart'),
    path('add_to_cart/<int:pk>', add_products_to_user_cart),
    path('delete_user_cart/<int:pk>', delete_user_cart),
    path('register/', RegisterUser.as_view(), name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
URL configuration for smartbazzar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import shop.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',shop.views.homepage,name='home'),
    path('register', shop.views.register, name='register'),
    path('login', shop.views.login_page, name='login'),
    path('cart', shop.views.cart_page, name='cart'),
    path('fav', shop.views.fav_page, name='fav'),
    path('favviewpage', shop.views.favviewpage, name='favviewpage'),
    path('logout', shop.views.logout_page, name='logout'),
    path('collection', shop.views.collection, name='collection'),
    path('collection/<str:name>', shop.views.collectionview, name='collection'),
    path('collection/<str:cname>/<str:pname>', shop.views.product_details, name='product_details'),
    path('addtocart', shop.views.add_to_cart, name='addtocart'),
    path('delete_cart/<int:cid>', shop.views.delete_cart, name='delete_cart'),
    path('delete_fav/<int:cid>', shop.views.delete_fav, name='delete_fav'),

]




urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
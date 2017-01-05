from django.conf.urls import include, url
from django.contrib import admin

from bitcoin_emulation.apps.core import views as core_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', core_views.loginview),
    url(r'^logout/', core_views.logoutview),
    url(r'^auth/', core_views.auth_and_login),
    url(r'^signup/', core_views.sign_up_in),
    url(r'^shop/', core_views.shop),
    url(r'^add-product/', core_views.add_product),
    url(r'^buy-product/(?P<product_id>[0-9]+)/', core_views.buy_product),
    url(r'^create-first/', core_views.create_first),
    url(r'^mine/', core_views.mine),
    url(r'^$', core_views.user_cabinet)
]

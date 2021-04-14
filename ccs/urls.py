from django.contrib import admin
from pages import views as pages_views
from users import views as users_views
from blog import views as blog_views
from cart import views
from accounts import views
from orders import views
from payment import views
from django.urls import path, include
from django.views.generic.base import TemplateView
# from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic import RedirectView



# from pages.views import (
#     home_view, 
#     contact_view, 
#     about_view, 
#     social_view,
    
#     )


urlpatterns = [
    
    path('courses/', include('courses.urls')),
    path('about/', pages_views.about_view, name='about'),
    path('contact/', pages_views.contact_view),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    
    path('admin/', admin.site.urls),
    path('social/', pages_views.social_view, name = 'social'),
    path('profile/', pages_views.profile_view, name = 'profile'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('feedback/', blog_views.feedback, name='feedback'),
    path('dashboard/', users_views.dashboard, name='dashboard'),
    path('register/', users_views.register, name='register'),
    path('dashboard/', include('django.contrib.auth.urls')),
    path('media/', include('media.urls')),
    #url(r'^cart/', include('cart.urls')),
    url(r'^cart/', include(('cart.urls','cart') ,namespace='cart')),
    url(r'^orders/', include(('orders.urls', 'orders'),namespace='orders')),
    url(r'^payment/', include(('payment.urls','payment'), namespace='payment')),
    url(r'^coupons/', include(('coupons.urls','coupons'), namespace='coupon')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    #url(r'^create/$', orders_views.OrderCreate, name='OrderCreate'),
    #url(r'^admin/order/(?P<order_id>\d+)/$', orders_views.AdminOrderDetail, name='AdminOrderDetail'),
    #url(r'^admin/order/(?P<order_id>\d+)/pdf/$', orders_views.AdminOrderPDF, name='AdminOrderPDF'),

    url(r'^rosetta/', include('rosetta.urls')),
    #url(r'^', include('shop.urls', namespace='shop')),
    
    url(r'^', include(('shop.urls','shop'), namespace='shop'))

    #url(r'^chat/', include('chatrooms.urls')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



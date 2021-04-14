from django.contrib import admin
from django.conf import settings # new
from django.urls import path # new
from django.conf.urls.static import static # new


app_name = 'media'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('media/', include('media.urls')), # new
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
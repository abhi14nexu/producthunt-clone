
from django.contrib import admin
from django.urls import path,include
from . import settings
import products.views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',products.views.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path,include
from . import settings
import products.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',products.views.home,name='home'),
    path('accounts/',include('accounts.urls'))
]

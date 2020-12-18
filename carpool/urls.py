
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/' , include('logPage.urls')),
    path('rider/', include('rider.urls')),
    path('driver/' , include('driver.urls'))
]

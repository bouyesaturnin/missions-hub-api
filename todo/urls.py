from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', auth_views.obtain_auth_token),
    path('api/', include('myapp.urls')), # <--- Vérifie bien cette ligne
]


# AJOUTE CETTE LIGNE :
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

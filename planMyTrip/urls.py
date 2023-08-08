from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from planner.views import save_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('user.urls')),
    path('', include('planner.urls')),
    path('save_pdf/', save_pdf, name='save_pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

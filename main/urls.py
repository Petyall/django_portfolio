from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from portfolio_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:project_id>', views.detail, name='detail'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from main.views import home

urlpatterns = [
  path('', home, name='home'),
  path('search/', include(('my_app.urls', 'my_app'), namespace='search')),
  path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
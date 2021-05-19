from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    url(r'^', include("apps.gifs.urls", namespace="gifs")),
    url(r'^', include("apps.tags.urls", namespace="tags")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
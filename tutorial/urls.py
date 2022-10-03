from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

router = routers.DefaultRouter()

# router.register('devices', FCMDeviceAuthorizedViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

    path("admin/", admin.site.urls),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # api
    path('api/users/', include('users.urls')),
    path('api/pushnotification/', include('push_notifications.urls')),
    path("api/posts/", include("posts.urls")),
    path("api/todos/", include("todos.urls")),
    path("api/chats/", include("chats.urls")),
    path("api/redirects/", include("redirects.urls"))
]
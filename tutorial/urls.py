from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

    path("admin/", admin.site.urls),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # api authentication and token generation
    # path("user/", include("accounts.urls", namespace="accounts")),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # api
    path('api/users/', include('users.urls')),
    path("api/posts/", include("posts.urls", namespace="posts_api")),
    path("api/chats/", include("chats.urls", namespace="chats_api")),
]
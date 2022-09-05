from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path, re_path
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers, serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()

urlpatterns = [
    # path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/polls/", include("polls.urls")),
    # API SCHEMA
    # ==========================================
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

user_router = routers.SimpleRouter()
user_router.register("users", UserViewSet)
auth_patterns = user_router.urls

# 除外 URL name
omit_url_names = (
    "user-list",
    "user-detail",
    "user-me",
    "user-set-username",
)
auth_patterns = [pat for pat in auth_patterns if pat.name not in omit_url_names]

user_list_view = UserViewSet.as_view({"post": "create"}, **{"suffix": "List", "basename": "user", "detail": False})
auth_patterns += [re_path("^users/$", user_list_view, name="user-list")]

urlpatterns += [path("api/auth/", include(auth_patterns)), path("api/auth/", include("djoser.urls.authtoken"))]

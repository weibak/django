# api/urls.py

from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.profiles.views import ProfileViewSet
from api.shop.views import PurchaseCreateView, ProductViewSet
from api.users.views import UserCreateView, UserLoginView, UserLogoutView, UserViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"profiles", ProfileViewSet)
router.register(r"products", ProductViewSet, basename="products")
router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path(
        "products/<int:product_id>/purchase",
        PurchaseCreateView.as_view(),
        name="purchase",
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

from django.conf import settings
from rest_framework.routers import SimpleRouter, DefaultRouter

from redvot.login.views import LoginViewSet, LogoutViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("login", LoginViewSet, "login")
router.register("logout", LogoutViewSet, "logout")

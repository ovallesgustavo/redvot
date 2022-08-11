from redvot.common.default_router import DefaultRouter
from redvot.login.urls import router as login

# if settings.DEBUG:
main_router = DefaultRouter()

main_router.extend(login)

app_name = "redvot"
urlpatterns = main_router.urls

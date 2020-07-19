from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.viewsets import (
    GuildViewSet,
    GuildConfigViewSet,
    RoleViewSet,
    UserViewSet
)


router = DefaultRouter()

router.register('guilds', GuildViewSet)
router.register('guild_configs', GuildConfigViewSet)
router.register('roles', RoleViewSet)
router.register('users', UserViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls))
]

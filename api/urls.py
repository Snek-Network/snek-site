from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.viewsets import (
    GuildViewSet,
    GuildConfigViewSet,
    InfractionViewSet,
    RoleViewSet,
    UserViewSet
)


router = DefaultRouter(trailing_slash=False)

router.register('guilds', GuildViewSet)
router.register('guild_configs', GuildConfigViewSet)
router.register('infractions', InfractionViewSet)
router.register('roles', RoleViewSet)
router.register('users', UserViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls))
]

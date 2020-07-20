from django.contrib import admin

from api.models import Guild, GuildConfig, Infraction, Role, User


admin.site.register(Guild)
admin.site.register(GuildConfig)
admin.site.register(Infraction)
admin.site.register(Role)
admin.site.register(User)

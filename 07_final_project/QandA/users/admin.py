from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site

from users.models import CustomUser


admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id', )
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name', )
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)


class CustomUserAdmin(UserAdmin):

    # add_form =
    # form = 

    model = CustomUser
    list_display = [
        'username',
        'email',
        'is_staff'
    ]


admin.site.register(CustomUser)

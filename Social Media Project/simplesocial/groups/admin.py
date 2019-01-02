from django.contrib import admin
from . import models


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
    # with this, when we use admin page, we can click on Group and see all members etc.

admin.site.register(models.Group)

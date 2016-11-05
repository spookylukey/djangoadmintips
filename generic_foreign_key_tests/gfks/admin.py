from django.contrib import admin

from .models import Group, Person, Task


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        qs = qs.select_related('owner_type')
        # Can't do select related for owner or owner_id
        # because they are not DB foreign keys.

        # We can use prefetch_related on the GFK.
        qs = qs.prefetch_related('owner')

        # But we can't do the following, because not all objects have
        # 'creator':
        # qs = qs.prefetch_related('owner__creator')
        return qs


admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Task, TaskAdmin)

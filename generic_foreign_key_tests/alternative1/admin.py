from django.contrib import admin

from .models import Group, Person, Task


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        qs = qs.select_related('owner_group',
                               'owner_person',
                               'owner_group__creator')
        return qs


admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Task, TaskAdmin)

from django.contrib import admin

from .models import Group, Person, Task


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        qs = qs.select_related('owner__group',
                               'owner__group__creator',
                               'owner__person')
        return qs


admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Task, TaskAdmin)

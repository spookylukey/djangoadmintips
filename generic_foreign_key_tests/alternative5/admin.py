from django.contrib import admin

from .models import Group, Person, GroupTask, PersonTask


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        qs = qs.select_related('owner')
        return qs


class GroupTaskAdmin(TaskAdmin):
    def get_queryset(self, request):
        qs = super(GroupTaskAdmin, self).get_queryset(request)
        qs = qs.select_related('owner__creator')
        return qs


class PersonTaskAdmin(TaskAdmin):
    pass


admin.site.register(Group)
admin.site.register(Person)
admin.site.register(GroupTask, GroupTaskAdmin)
admin.site.register(PersonTask, PersonTaskAdmin)

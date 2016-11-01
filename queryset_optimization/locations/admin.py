from django.contrib import admin

from .models import Location

# This comes from a StackOverflow question:
# “Different queryset optimisation for list view and change view in Django Admin”
# http://stackoverflow.com/questions/40054325/different-queryset-optimisation-for-list-view-and-change-view-in-django-admin


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['owner', 'postcode']
    fields = ['owner', 'postcode', 'tenants']
    filter_horizontal = ['tenants']

    def get_queryset(self, request):
        qs = super(LocationAdmin, self).get_queryset(request)
        qs = qs.select_related('owner__user')
        if request.resolver_match.func.__name__ == 'change_view':
            qs = qs.prefetch_related('tenants')
        return qs

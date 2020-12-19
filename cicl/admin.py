from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Document, Isotope, Researcher, Parameter


admin.site.site_header = 'Canadian Ice Core Lab Admin Dashboard'


class DocumentAdmin(admin.ModelAdmin):
    filter_horizontal = ('isotopes', 'parameters', 'researchers')
    list_display = ('core_name', 'created', 'document_id')
    list_filter = ('created',)


class IsotopeAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('type',)


class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')


# Register User-defined Models
admin.site.register(Document, DocumentAdmin)
admin.site.register(Isotope, IsotopeAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Researcher, ResearcherAdmin)

# Unregister Built-in Django Models
admin.site.unregister(Group)

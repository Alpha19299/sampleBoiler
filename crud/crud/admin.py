from django.contrib import admin
from crud.models import DetailsModel
from import_export.admin import ExportActionMixin


class DetailsAdmin(ExportActionMixin, admin.ModelAdmin):
    pass

admin.site.register(DetailsModel, DetailsAdmin)
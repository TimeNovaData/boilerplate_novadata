from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class BaseNovadataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

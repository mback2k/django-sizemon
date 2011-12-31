from django.contrib import admin
from sizemon.models import Snapshot, Path

class SnapshotAdmin(admin.ModelAdmin):
    list_filter = ('crdate',)
    list_display = ('crdate',)
    ordering = ('crdate',)

class PathAdmin(admin.ModelAdmin):
    fields = ('path', 'size', 'snapshot')
    list_display = ('path', 'size', 'snapshot')
    ordering = ('snapshot', 'path', 'size')

admin.site.register(Snapshot, SnapshotAdmin)
admin.site.register(Path, PathAdmin)

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(categories)

class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    readonly_fields = ('slug',)

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        obj.save()

admin.site.register(MediaContent, MediaAdmin)

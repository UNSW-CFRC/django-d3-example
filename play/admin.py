from django.contrib import admin


from .models import Play


admin.site.register(Play)

class PlayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

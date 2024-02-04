from django.contrib import admin
from .models import About, SocialLink


# This is to make the add button to disappear from the admin panel so that we will be unable to add another about
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)

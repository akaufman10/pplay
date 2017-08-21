from django.contrib import admin
from .models import Play, Submission, UserProfile
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['submitter', 'read','read_by']
    ordering = ['submitter']
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        rows_updated = queryset.update(read='r')
        if rows_updated == 1:
            message_bit = "1 submission was"
        else:
            message_bit = "%s submission were" % rows_updated
        self.message_user(request, "%s successfully marked as read." % message_bit)
    mark_as_read.short_description = "Mark submission as read"

class PlayAdmin(admin.ModelAdmin):
        
        
        
    
        def save_model(self, request, obj, form, change): 
            obj.logo = request.user.userprofile.icon
            obj.save()


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PlayerInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'player'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PlayerInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Submission,SubmissionAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


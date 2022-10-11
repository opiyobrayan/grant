from django.contrib import admin
from . models import Grant,Post,Activity,ActivityType,Thematic,ThematicMember
# Register your models here.
admin.site.register(Grant)
admin.site.register(Post)
admin.site.register(ThematicMember)
admin.site.register(Thematic)
admin.site.register(ActivityType)
admin.site.register(Activity)
from django.contrib import admin
from .models import skills,overview,Education,Acheivements,certifications,projects,FilesAdmin
# Register your models here.
admin.site.register(skills)
admin.site.register(overview)
admin.site.register(Education)
admin.site.register(Acheivements)
admin.site.register(certifications)
admin.site.register(projects)
admin.site.register(FilesAdmin)
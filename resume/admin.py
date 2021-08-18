from django.contrib import admin
from .models import Bio, School, SkillSet, Contact_form

# Register your models here.

admin.site.register(Bio)
admin.site.register(School)
admin.site.register(SkillSet)
admin.site.register(Contact_form)
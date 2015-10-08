from django.contrib import admin

# Register your models here.
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'updated')

admin.site.register(SignUp, SignUpAdmin)

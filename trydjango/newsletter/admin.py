from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
	""" customizes the look of admin for SignUp """
    list_display = ('email', 'timestamp', 'updated')
    
    # the Meta, in this case, allows for the list_display
    class Meta:
    	model = SignUp

    form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)

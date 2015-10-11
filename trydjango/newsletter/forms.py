from django import forms

from .models import SignUp

# customizes the admin form (aka model form)
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = [ 'full_name', 'email' ]

	# model forms in general do some checks before allowing changes to the database
	# when writing 'clean_' methods, you must follow with the field name for it to work
	# overriding/checking the function for clean email data
	# self is for that single instance of that form
	def clean_email(self):
		# print(self.cleaned_data)
		email = self.cleaned_data.get('email')

		# # this will only check for edu anywhere in email
		# if not "edu" in email:
		# 	raise forms.ValidationError("Please use a valid 'EDU' address")

		# # this will check for the correct EDU extension
		# without specificity for domain, edu.com will still work
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		if not domain == 'osu':
			raise forms.ValidationError("Please make sure you use your 'OSU' email.")
		if not "edu" in email:
			raise forms.ValidationError("Please use a valid 'EDU' address.")
		return email


	# example full_name template (the code below is already the default)
	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		# write validation code here. 
		if not " " in full_name:
			raise forms.ValidationError("Please write first and last name")
		return full_name


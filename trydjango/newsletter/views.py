from django.shortcuts import render

from .forms import SignUpForm

# Create your function based views.
def home(request):

	# title is requesting and responding
	title = "välkommen"

	# return render(request, "home.html", {})
	if request.user.is_authenticated():
		title = "välkommen {}".format(request.user)

	question = "How goes it today?"
	status = ""

	# the None does not instantly show the .errorlist li (ie. validators)
	form = SignUpForm(request.POST or None)

	context = {
		"title": title, 
		"question": question,
		"form": form,
	}

	# test the POST method
	if request.method == "POST":
		print(request.POST, "before validation")

	if form.is_valid():
		submittal_data = form.save(commit=False) # pauses the submit
		
		# commit=False provides a gap of time until save() for code
		# w/o commit = false ---> form.save() still runs validators

		# option 1 to change name:
		# if submittal_data.full_name == None:
		# 	submittal_data.full_name == "Michael Williams"

		# option 2 to change name:
		full_name = form.cleaned_data.get("full_name")
		if not "z" in full_name:
			full_name = full_name + "z"
		submittal_data.full_name = full_name

		submittal_data.save() # actually saves it
		print(submittal_data, "after validation")
		print(submittal_data.email, submittal_data.timestamp)

		context = {
			"status": "Thank you."
		}

	return render(request, "home.html", context)
	

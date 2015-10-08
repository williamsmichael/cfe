from django.shortcuts import render

# Create your function based views.
def home(request):
	return render(request, "home.html", {})

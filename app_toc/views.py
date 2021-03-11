from django.shortcuts import render

def tocview(request):
	return render(request, "toc.html", {'a':'7'})
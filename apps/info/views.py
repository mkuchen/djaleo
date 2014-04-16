from django.shortcuts import render
from django.views.generic import View
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

class HomeView(View):
	template_name = 'info/home.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)
from django.shortcuts import render
from django.views.generic import View
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

class HomeView(View):
	template_name = 'info/home.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class TwoView(View):
	template_name = 'info/home2.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)



""" CATH VIEWS BEGIN """

class CathHomeView(View):
	template_name = 'info/cath/cathie_home.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class CathAboutView(View):
	template_name = 'info/cath/cathie_about.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class CathClassesView(View):
	template_name = 'info/cath/cathie_classes.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class CathOneView(View):
	template_name = 'info/cath/cathie_one_on_one.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class CathLocationsView(View):
	template_name = 'info/cath/cathie_locations.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


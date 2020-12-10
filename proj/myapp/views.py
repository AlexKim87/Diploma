from datetime import datetime
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Module, Controller, Slot, ControllerModule


# Create your views here.

class ControllerFormFillingView(View):

	def get(self, request):

		controllers = Controller.objects.all()
		controller_types = []
		for controller in controllers:
			try:
				if controller.controller_type in controller_types:
					continue
				else:
					controller_types.append(controller.controller_type)
			except:
				pass

		return render(request, 'myapp/controller_form_filling.html', {'controller_types': controller_types})


class ControllerSearchView(View):

	def get(self, request):

		controllers = Controller.objects.all()
		controller_types = []
		for controller in controllers:
			try:
				if controller.controller_type in controller_types:
					continue
				else:
					controller_types.append(controller.controller_type)
			except:
				pass

		return render(request, 'myapp/controller_search.html', {'controller_types': controller_types})


class ControllersListView(View):

	def get(self, request):

		a = ['--' for i in range(23)]

		controller = Controller.objects.all()

		controllers = []
		controller_types = []
		qc_dates = []
		project_names = []

		for cont in controller:

			slots = Slot.objects.select_related().all().filter(
				controller_module__controller__factory_number=cont.factory_number).order_by('slot_number')

			new_slots = [None for i in range(1, 15)]
			j = 0

			for i in range(1, 15):
				try:
					if slots[j].slot_number == i:
						new_slots[i-1] = slots[j]
						j += 1
				except:
					pass
			controllers.append({'controller': cont, 'slot': new_slots})

			try:
				if cont.controller_type in controller_types:
					continue
				else:
					controller_types.append(cont.controller_type)
			except:
				pass

			try:
				if cont.qc_date.year in qc_dates:
					continue
				else:
					qc_dates.append(cont.qc_date.year)
			except:
				pass

			try:
				if cont.project_name in project_names:
					continue
				else:
					project_names.append(cont.project_name)
			except:
				pass

		return render(request, 'myapp/controllers_list.html', {'controllers': controllers,
																'a': a,
																'controller_types': controller_types,
																'qc_dates': qc_dates,
																'project_names': project_names})


class ModulePassportFillingView(View):

	def get(self, request):

		modules = Module.objects.all()
		module_names = []
		for module in modules:
			try:
				if module.module_name in module_names:
					continue
				else:
					module_names.append(module.module_name)
			except:
				pass

		return render(request, 'myapp/module_passport_filling.html', {'module_names': module_names})


class ModuleSearchView(View):

	def get(self, request):

		modules = Module.objects.all()
		module_names = []
		for module in modules:
			try:
				if module.module_name in module_names:
					continue
				else:
					module_names.append(module.module_name)
			except:
				pass

		return render(request, 'myapp/module_search.html', {'module_names': module_names})


class ModulesListView(View):

	def get(self, request):

		modules = Module.objects.all()

		modules_controllers = []
		original_module_names = []
		original_production_years = []

		for module in modules:
			try:

				controller_module = ControllerModule.objects.select_related().all().filter(module__factory_number=module.factory_number)

				modules_controllers.append({'module': module, 'controller': controller_module[0].controller})

			except:
				modules_controllers.append({'module': module, 'controller': None})

			try:
				if module.module_name in original_module_names:
					continue
				else:
					original_module_names.append(module.module_name)
			except:
				pass

			try:
				if module.production_date.year in original_production_years:
					continue
				else:
					original_production_years.append(module.production_date.year)
			except:
				pass

		return render(request, 'myapp/modules_list.html', {'modules_controllers': modules_controllers,
														   'original_module_names': original_module_names,
														   'original_production_years': original_production_years})


class ProjectFormsFillingView(View):

	def get(self, request):
		return render(request, 'myapp/project_forms_filling.html')

# class WebsiteView(View):
#
# 	def get(self, request):
# 		return render(request, 'website/index.html')
#
# 	def post(self, request):
# 		d = request.POST['table_date'].split('.')
# 		d = f'{d[2]}-{d[1]}-{d[0]}'
# 		t = request.POST['table_time']
# 		n = request.POST['table_name']
#
# 		booking = BookTable(name=n, date=d, time=t)
# 		booking.save()
# 		return render(request, 'website/index.html')
#
#
# class MenuView(View):
#
# 	def get(self, request):
# 		return render(request, 'website/menu.html')
#
# 	def post(self, request):
# 		html = '<html><body>'
# 		for key, value in request.POST.items():
# 			html += f'{key}:{value}<br>'
# 		html += '</body></html>'
# 		return HttpResponse(html)
#
#
# class ContactView(View):
#
# 	def get(self, request):
# 		return render(request, 'website/contact-us.html')
#
# 	def post(self, request):
# 		n = request.POST['table_name']
# 		print(n)
# 		m = request.POST['table_message']
# 		s = request.POST['table_subject']
# 		me = request.POST['table_message']
#
# 		contact = Contact(name=n, mail=m, subject=s, message=me)
# 		contact.save()
# 		return render(request, 'website/contact-us.html')

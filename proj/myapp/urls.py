from django.urls import path, include
from django.http import HttpResponse
from .views import ControllerFormFillingView, ControllerSearchView,ControllersListView,\
	ModulePassportFillingView, ModuleSearchView, ModulesListView, ProjectFormsFillingView


from .models import Module, Controller, Slot


def get_controllers(request):

	controllers = Slot.objects.select_related()

	response = '<body>'
	for controller in controllers:
		response += f'{controller}<br>'
	response += '</body>'
	return HttpResponse(response)




urlpatterns = [

	path('controller_form_filling/', ControllerFormFillingView.as_view(), name='controller_form_filling'),
	path('controller_search/', ControllerSearchView.as_view(), name='controller_search'),
	path('controllers_list/', ControllersListView.as_view(), name='controllers_list'),
	path('module_passport_filling/', ModulePassportFillingView.as_view(), name='module_passport_filling'),
	path('module_search/', ModuleSearchView.as_view(), name='module_search'),
	path('modules_list/', ModulesListView.as_view(), name='modules_list'),
	path('project_forms_filling/', ProjectFormsFillingView.as_view(), name='project_forms_filling'),
	path('simple_controllers/', get_controllers),

]

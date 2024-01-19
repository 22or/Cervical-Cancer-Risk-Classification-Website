from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
import requests
from . import forms
import numpy
import pandas

# Create your views here.
def index(request):
	return render(request,'assessments/index.html')

class AssessmentFormView(FormView):
	template_name = 'assessments/assessment.html'
	form_class = forms.AssessmentForm
	success_url = reverse_lazy('results')

	def form_valid(self,form):
		individual = []
		for key in form.cleaned_data:
			individual.append(form.cleaned_data[key])
		individual = pandas.DataFrame([individual]).values
		model_request = {
			'inputs': [
				# StringCodec.encode_input(name = 'columns',payload = individual[0],use_bytes = False).dict(),
				# StringCodec.encode_input(name = 'values',payload = [str(i) for i in individual[1]],use_bytes = False).dict()
				{
					'name': 'predict',
					'shape': individual.shape,
					'datatype': 'FP32',
					'data': individual.tolist()
				}
			],
			'outputs': [
				{'name': 'predict_proba'}
			]
		}
		r = requests.post('http://0.0.0.0:8080/v2/models/risk-model/infer',json = model_request)
		# return HttpResponse(r.json().get('outputs')[0].get('data')[1])
		
		return HttpResponseRedirect(self.success_url + '?result=' + str(r.json().get('outputs')[0].get('data')[1]))
	
def results(request):
	return HttpResponse(request.GET.get('result'))
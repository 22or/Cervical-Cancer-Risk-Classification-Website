from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AssessmentForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'
		self.helper.form_class= 'form-horizontal'
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit','Submit'))
	
	age = forms.IntegerField()
	number_of_sexual_partners = forms.IntegerField()
	first_sexual_intercourse = forms.IntegerField()
	num_of_pregnancies = forms.IntegerField()
	smokes = forms.BooleanField(required=False)
	years_of_smoking = forms.IntegerField()
	smokes_packs_per_year = forms.IntegerField()
	hormonal_contraceptives = forms.BooleanField(required=False)
	years_of_hormonal_contraceptives = forms.IntegerField()
	iud = forms.BooleanField(required=False)
	iud_years = forms.IntegerField()
	stds = forms.BooleanField(required=False)
	stds_number = forms.IntegerField()
	condylomatosis = forms.BooleanField(required=False)
	cervical_condylomatosis = forms.BooleanField(required=False)
	vaginal_condylomatosis = forms.BooleanField(required=False)
	vulvo_perineal_condylomatosis = forms.BooleanField(required=False)
	syphilis = forms.BooleanField(required=False)
	pelvic_inflammatory_disease = forms.BooleanField(required=False)
	genital_herpes = forms.BooleanField(required=False)
	molluscum_contagiosum = forms.BooleanField(required=False)
	aids = forms.BooleanField(required=False)
	hiv = forms.BooleanField(required=False)
	hepatitis_b = forms.BooleanField(required=False)
	hpv = forms.BooleanField(required=False)
	number_of_diagnosis  = forms.IntegerField()
	cervical_dysplasia_diagnosis = forms.BooleanField(required = False)
	hpv_diagnosis = forms.BooleanField(required = False)
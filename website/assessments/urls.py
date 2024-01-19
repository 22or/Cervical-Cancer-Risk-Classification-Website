from django.urls import path
from . import views

urlpatterns = [
	path('',views.AssessmentFormView.as_view(),name = 'assessment'),
	path('results/',views.results,name = 'results')
]
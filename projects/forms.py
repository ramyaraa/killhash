from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = ['title','featured_image', 'description', 'demo_link', 'source_link', 'tags']
    widgets = {
      # thsi is change the ugle check box to beautefle one
      'tags': forms.CheckboxSelectMultiple(),
    }
  def __init__(self, *args, **kwargs):
    super(ProjectForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'input'})

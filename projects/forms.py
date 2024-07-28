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
    self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
    #this a for loop for throuing all item and add a class  input
    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'input'})
    # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Description'})
    # self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Demo Link'})
    

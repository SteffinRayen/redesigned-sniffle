from django import forms
from .models import ErrorData


class ErrorForm(forms.ModelForm):
    class Meta:
        model = ErrorData
        fields = ('module_id', 'error_id', 'error_name', 'error_description', 'error_mitigation',
                  'screenshot_link', 'author', 'error_validated', 'error_validator', 'editors_list', )

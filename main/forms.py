from django import forms

from main.models import Student, Subject


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentForm(FormStyleMixin, forms.ModelForm):


    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email')
        # exclude = ('is_active',)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if '@sky.pro' not in cleaned_data:
            raise forms.ValidationError('Почта должна быть от учебного заведения')

        return cleaned_data



class SubjectForm(FormStyleMixin, forms.ModelForm):


    class Meta:
        model = Subject
        fields = '__all__'

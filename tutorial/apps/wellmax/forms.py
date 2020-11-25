from django import forms
from .models import UserServiceEvaluation, UserInfo


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(
                attrs={
                    'class': 'custom-control-input custom-control-label',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control ',
            'name': 'full_name',
            'required': 'required',
            'placeholder': 'Ф.И.О'
        })
        self.fields['gender'].widget.attrs.update({
            'class': 'custom-control-input',
            'name': 'gender',
            'required': 'required',
        })
        self.fields['room'].widget.attrs.update({
            'class': 'form-control ',
            'name': 'room',
            'required': 'required',
            'placeholder': 'Номер комнаты '
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'name': 'phone',
            'id': 'phone',
            'value': '+998 ',
            'required': 'required',
        })


class UserServiceEvaluationForm(forms.ModelForm):

    class Meta:
        model = UserServiceEvaluation
        fields = '__all__'
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['service1_rank'].widget.attrs.update({
            'class': 'custom-select',
            'name': 'service1_rank',
            'required': 'required',
        })
        self.fields['service2_rank'].widget.attrs.update({
            'class': 'custom-select',
            'name': 'service2_rank',
            'required': 'required',
        })
        self.fields['service3_rank'].widget.attrs.update({
            'class': 'custom-select',
            'name': 'service3_rank',
            'required': 'required',
        })
        self.fields['service4_rank'].widget.attrs.update({
            'class': 'custom-select',
            'name': 'service4_rank',
            'required': 'required',
        })
        self.fields['feedback'].widget.attrs.update({
            'class': 'form-control',
            'name': 'feedback',
            'rows': '5',
        })
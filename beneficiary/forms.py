from django import forms
from . import models

class GetBeneficiaryDataForm(forms.Form):

    

    def __init__(self, *args, **kwargs):
        super(GetBeneficiaryDataForm, self).__init__(*args, **kwargs)
        scheme_pk_list = [u['pk'] for u in models.Scheme.objects.all().values('pk')]

        SCHEME_CHOICES = []
        for scheme_pk in scheme_pk_list:
            SCHEME_CHOICES.append((scheme_pk, models.Scheme.objects.get(pk__exact=scheme_pk).name))
        
        self.fields['scheme'] = forms.ChoiceField(label='Scheme' ,choices=SCHEME_CHOICES)


class AddApplicantForm(forms.ModelForm):

    class Meta():
        model = models.Applicant
        exclude = ['is_approved_rent', 'is_approved_clerk', 'is_approved_adc', 'is_disapproved']



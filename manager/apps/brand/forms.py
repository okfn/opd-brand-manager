from django import forms
from .models import BrandType
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from captcha.fields import ReCaptchaField


class ProposalReviewForm(forms.ModelForm):
    moderator_comment = forms.CharField(widget=forms.Textarea, max_length=255,
                                        label='Your comments', required=False)
    is_valid = forms.BooleanField(label='Brand is valid', initial=True,
                                  required=False)

    def __init__(self, *args, **kwargs):
        super(ProposalReviewForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.fields['moderator_comment'].initial = \
                kwargs['instance'].moderator_comment \
                if hasattr(kwargs['instance'], 'moderator_comment') \
                else ''

            if hasattr(kwargs['instance'], 'moderator_validated'):
                self.fields['is_valid'].initial = \
                    True if kwargs['instance'].moderator_validated else False


class BrandProposalForm(forms.Form):
    brand_nm = forms.CharField(max_length=255, label='Brand name')
    brand_type = forms.ModelChoiceField(queryset=BrandType.objects.all())
    # Postponed in ticket #58
    #owner_nm = forms.CharField(
    #    max_length=255, label='Owner name', required=False)
    brand_link = forms.URLField(
        max_length=255, label='Brand website', required=False)
    brand_logo = forms.ImageField(
        label='Brand logo', required=False)
    comments = forms.CharField(widget=forms.Textarea, max_length=255,
                               label='Comments', required=False)
    sender = forms.EmailField(max_length=255, label='Your mail')
    captcha = ReCaptchaField()

    def clean_brand_logo(self):
        logo = self.cleaned_data['brand_logo']
        if logo:
            file_type = logo.content_type.split('/')[0]

            if len(logo.name.split('.')) == 1:
                raise forms.ValidationError('File type is not supported')

            if file_type in settings.TASK_UPLOAD_FILE_TYPES:
                if logo._size > settings.TASK_UPLOAD_FILE_MAX_SIZE:
                    raise forms.ValidationError(
                        'Please keep filesize under %s. Current filesize %s.'
                        % (filesizeformat(settings.TASK_UPLOAD_FILE_MAX_SIZE),
                           filesizeformat(logo._size)))
            else:
                raise forms.ValidationError('File type is not supported')

        return logo

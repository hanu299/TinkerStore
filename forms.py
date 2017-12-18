from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='')
    from_email = forms.EmailField(required=True, label='')
    number = forms.CharField(required=True, label='')
    message = forms.CharField(label='')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Name '
        self.fields['from_email'].widget.attrs['placeholder'] = 'Enter Your Email Address'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter Your Message'
        self.fields['number'].widget.attrs['placeholder'] = 'Enter You Number Here'

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Name")
    subject = forms.CharField(required=True, label="Subject")
    email = forms.EmailField(required=True, label="Email")
    mobile = forms.CharField(required=False, label="Mobile")
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message",
        max_length = 1020
    )
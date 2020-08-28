from django import forms


class AskQuestionForm(forms.Form):
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    product = forms.IntegerField(required=False)

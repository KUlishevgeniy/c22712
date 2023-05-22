from django import forms


class TestForm(forms.Form):
    test_data = forms.CharField(label="test data", max_length=128)

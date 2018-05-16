from django import forms
from .models import *

class BookAdminForm(forms.ModelForm):
    quantity = forms.IntegerField(disabled=True, initial=0)
    class Meta:
        model = Book
        fields = '__all__'

class CopyAdminForm(forms.ModelForm):
    class Meta:
        model = Copy
        fields = '__all__'

    def clean(self):
        super(CopyAdminForm, self).clean()
        book = self.cleaned_data['book']
        book.quantity += 1
        book.save()

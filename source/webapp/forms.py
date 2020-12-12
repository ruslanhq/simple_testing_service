from django import forms


class AnswerInlineFormSet(forms.BaseInlineFormSet):

    def clean(self):
        super().clean()
        for form in self.forms:
            if form.cleaned_data.get('is_valid'):
                return
        raise forms.ValidationError("Должен быть хотя бы 1 правильный ответ.")


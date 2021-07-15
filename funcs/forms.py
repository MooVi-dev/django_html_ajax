import datetime
from django import forms

cur_year = datetime.datetime.now().year


class CheckDate(forms.Form):
    over_cur_year = forms.BooleanField(required=False)
    year = forms.IntegerField(max_value=3999, min_value=1900)
    hidden_error = forms.HiddenInput()

    def clean(self):
        cleaned_data = super(CheckDate, self).clean()
        over_cur_year = cleaned_data.get("over_cur_year")
        year = cleaned_data.get("year")

        if year == 2018:
            self.hidden_error = 'Год не должен быть равен 2018'
            raise forms.ValidationError('Год не должен быть равен 2018')
        elif year <= cur_year or over_cur_year:
            pass
        else:
            self.hidden_error = 'Введенный год не больше текущего'
            raise forms.ValidationError('Введенный год не больше текущего')
        return cleaned_data

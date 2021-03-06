from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class QuestionForm(forms.Form):
    question = forms.CharField(label='question', max_length=1000)
    ans_1 = forms.CharField(label='ans_1', max_length=400)
    ans_2 = forms.CharField(label='ans_2', max_length=400)
    ans_3 = forms.CharField(label='ans_3', max_length=400)
    ans_4 = forms.CharField(label='ans_4', max_length=400)



class DatetimeForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )





class dateForm(forms.Form):
    date_field = forms.DateField(widget=DatePicker())
    date_field_required_with_min_max_date = forms.DateField(
        required=True,
        widget=DatePicker(options={
            'minDate': '2009-01-20',
            'maxDate': '2017-01-20',
        }, ),
        initial='2013-01-01',
    )
    """
    In this example, the date portion of defaultDate is irrelevant;
    only the time portion is used. The reason for this is that it has
    to be passed in a valid MomentJS format. This will default the time
    to be 14:56:00 (or 2:56pm).
    """
    time_field = forms.TimeField(widget=TimePicker(
        options={
            'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
            'defaultDate': '1970-01-01T14:56:00'
        },
        attrs={
            'input_toggle': True,
            'input_group': False,
        },
    ), )
    datetime_field = forms.DateTimeField(widget=DateTimePicker(
        options={
            'useCurrent': True,
            'collapse': False,
        },
        attrs={
            'append': 'fa fa-calendar',
            'icon_toggle': True,
        }), )

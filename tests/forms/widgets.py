from decimal import Decimal

from django import forms

import material
from material import (
    Icon, Layout, Row, Span,
)


class CheckboxInputForm(forms.Form):
    title = 'CheckboxInput'
    subtitle = 'Widget options demo'

    field1 = forms.BooleanField(help_text='default', required=False)
    field2 = forms.BooleanField(help_text='initial value', initial=True)
    field3 = forms.BooleanField(help_text='disabled', disabled=True, initial=True)
    field4 = forms.BooleanField(help_text='on a row with textfield')
    textfield = forms.CharField(
        help_text='with boolean',
        widget=material.TextInput(prefix=Icon('edit'))
    )

    layout = Layout(
        'field1',
        'field2',
        'field3',
        Row('textfield', Span('field4', desktop=3))
    )


class DecimalFieldForm(forms.Form):
    title = "Decimal"
    subtitle = 'Widget options demo'

    field1 = forms.DecimalField(help_text='default', required=False)
    field2 = forms.DecimalField(help_text='initial value', initial=Decimal('3.141592'))
    field3 = forms.DecimalField(help_text='value between 5-10', min_value=5, max_value=10)
    field4 = forms.DecimalField(help_text='digits restriction 99.999', max_digits=5, decimal_places=3)
    field5 = forms.DecimalField(help_text='disabled', disabled=True, initial=-1)
    field6 = forms.DecimalField(
        help_text='prefix',
        widget=material.NumberInput(prefix=Icon('insert_invitation')))


class EmailFieldForm(forms.Form):
    title = "Email"
    subtitle = 'Widget options demo'

    field1 = forms.EmailField(help_text='default', required=False)
    field2 = forms.EmailField(help_text='initial value', initial='john@doe.com')
    field3 = forms.EmailField(help_text='length between 10-20', min_length=10, max_length=20)
    field4 = forms.EmailField(help_text='disabled', disabled=True, initial='noreply@viewflow.io')
    field5 = forms.EmailField(
        help_text='prefix',
        widget=material.EmailInput(prefix=Icon('insert_invitation')))


class FloatFieldForm(forms.Form):
    title = "FloatField"
    subtitle = 'Widget options demo'

    field1 = forms.FloatField(help_text='default', required=False)
    field2 = forms.FloatField(help_text='initial value', initial=2.718282)
    field3 = forms.FloatField(help_text='value between 5-10', min_value=5, max_value=10)
    field4 = forms.FloatField(help_text='disabled', disabled=True, initial=-273.15)
    field5 = forms.FloatField(
        help_text='prefix',
        widget=material.NumberInput(prefix=Icon('insert_invitation'))
    )


class HiddenInputForm(forms.Form):
    title = "HiddenInput"
    subtitle = 'Widget options demo'

    field1 = forms.CharField(help_text='default', initial="hello!", widget=forms.HiddenInput)


class IntegerFieldForm(forms.Form):
    title = "IntegerField"
    subtitle = 'Widget options demo'

    field1 = forms.IntegerField(help_text='default', required=False)
    field2 = forms.IntegerField(help_text='initial value', initial=42)
    field3 = forms.IntegerField(help_text='value between 5-10', min_value=5, max_value=10)
    field4 = forms.IntegerField(help_text='disabled', disabled=True, initial=-1)
    field5 = forms.IntegerField(
        help_text='prefix',
        widget=material.NumberInput(prefix=Icon('insert_invitation')))
    field6 = forms.IntegerField(  # TODO
        help_text="range", widget=forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '100'}))


class PasswordInputForm(forms.Form):
    title = "PasswordInput"
    subtitle = 'Widget options demo'

    field1 = forms.CharField(
        help_text='default',
        required=False,
        widget=forms.PasswordInput)
    field2 = forms.CharField(
        help_text='prefix icon',
        initial="Initial value",
        widget=material.PasswordInput(prefix=Icon('lock'))
    )


class SelectForm(forms.Form):
    title = "Select"
    subtitle = 'Widget options demo'

    CHOICES = (
        (None, 'Select a fruit'),
        (1, 'Apple'),
        (2, 'Orange'),
        (3, 'Watermelon'))
    FLOAT_CHOICES = (
        (1.1, 'Perfect'),
        (1.0, 'Good'),
        (0.8, 'Bad'),
    )
    GROUPED_CHOICES = (
        (None, [(7, 'Mikhail')]),
        ('Team 1', [(1, 'Joe'), (2, 'Bob'), (3, 'Marie')]),
        ('Team 2', [(4, 'Anatoliy'), (5, 'Svetlana'), (6, 'Olga')]),
    )
    LONG_CHOICES = ((n, n) for n in range(100))

    field1 = forms.ChoiceField(help_text='default', choices=CHOICES, required=False)
    field2 = forms.ChoiceField(help_text='initial value', choices=CHOICES, initial=2)
    field3 = forms.ChoiceField(help_text='float choices', choices=FLOAT_CHOICES)
    field4 = forms.ChoiceField(help_text='groups', choices=GROUPED_CHOICES)
    field5 = forms.ChoiceField(help_text='long choices list', choices=LONG_CHOICES)
    field6 = forms.TypedChoiceField(help_text='coerce to int', coerce=int, choices=CHOICES)
    field7 = forms.ChoiceField(
        help_text='prefix',
        choices=CHOICES,
        widget=material.Select(prefix=Icon('account_box'))
    )
    field8 = forms.ChoiceField(help_text='on a row with textfield', choices=CHOICES)
    textfield = forms.CharField(
        help_text='with select',
        widget=material.TextInput(prefix=Icon('edit'))
    )
    field9 = forms.ChoiceField(
        help_text='disabled',
        disabled=True,
        choices=CHOICES,
        initial=3
    )

    layout = Layout(
        'field1',
        'field2',
        'field3',
        'field4',
        'field5',
        'field6',
        'field7',
        Row('textfield', Span('field8', desktop=3)),
        'field9'
    )


class TextInputForm(forms.Form):
    title = "TextInput"
    subtitle = 'Widget options demo'

    field1 = forms.CharField(help_text='default', required=False)
    field2 = forms.CharField(help_text='initial value', initial="Initial value")
    field3 = forms.CharField(help_text='length between 5-10', min_length=5, max_length=10)
    field4 = forms.CharField(
        help_text='prefix icon',
        widget=material.TextInput(prefix=Icon('edit'))
    )
    field5 = forms.CharField(
        help_text='suffix icon',
        widget=material.TextInput(suffix=Icon('perm_contact_calendar'))
    )
    field6 = forms.CharField(help_text='disabled', disabled=True, initial='Not editable')


class URLFieldForm(forms.Form):
    title = "URLField"
    subtitle = 'Widget options demo'

    field1 = forms.URLField(help_text='default', required=False)
    field2 = forms.URLField(help_text='initial value', initial="http://viewflow.io")
    field3 = forms.URLField(help_text='length between 10-100', min_length=10, max_length=100),
    field4 = forms.URLField(help_text='disabled', disabled=True, initial="http://viewflow.io/pro/")
    field5 = forms.URLField(
        help_text='prefix',
        widget=material.URLInput(prefix=Icon('insert_invitation')))

from django import forms

ORDER_TYPE = {
    ('S', 'Самовывоз'),
    ('D', 'Доставка'),
}
PAYMENT = {
    ('C', 'Карта'),
    ('Q', 'Qiwi'),
}
class CheckoutForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Andrey',
        'class': 'form-control',
    }))
    second_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Volodin',
        'class': 'form-control',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+7 (999) 123 4567',
        'class': 'form-control',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'г.Москва',
        'class': 'form-control',
    }))
    telegram = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
    }), required=False)
    payment = forms.ChoiceField(choices=ORDER_TYPE)
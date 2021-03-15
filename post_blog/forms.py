from django import forms
from .models import Post

### ModelForm uno:

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = [
#             'title',
#             'details',
#             'price',
#             'message'
#         ]

### ModelForm dos:

class PostForm(forms.ModelForm):

    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your title',
            }
        )
    )

    email = forms.EmailField()

    details = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                'id': 'id-de-textarea',
                'class': 'nombre-de-clase two',
                'placeholder': 'Your description',
                'rows': 14,
                'cols': 20,
            }
        ),
    )

    price = forms.DecimalField(initial=1.99)
    message = forms.CharField(initial='Hola que tal!')

    class Meta:
        model = Post
        fields = [
            'title',
            'details',
            'price',
            'message'
        ]

    """
    def clean_title(self, *args, **kwargs):
        default = 'sky'

        title = self.cleaned_data.get('title')

        if default not in title:
            raise forms.ValidationError(f'El titulo {title} ingresado no es igual a {default}, no es valido')

        if 'air' not in title:
            raise forms.ValidationError('El titulo ingresado no es valido')

        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        if not email.endswith('com'):
            raise forms.ValidationError('El email ingresado no es valido')

        return email
    """

### Form uno:

# class RawPostForm(forms.Form):
#     title = forms.CharField()
#     price = forms.DecimalField()
#     details = forms.CharField()
#     message = forms.CharField()

### Form dos:

class RawPostForm(forms.Form):

    title = forms.CharField(
        label='Titulo',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your title',
            }
        )
    )

    details = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                'id': 'id-de-textarea',
                'class': 'nombre-de-clase two',
                'placeholder': 'Your description',
                'rows': 14,
                'cols': 20,
            }
        ),
    )

    price = forms.DecimalField(initial=0.99)
    message = forms.CharField()

from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    
    title       = forms.CharField(label = '', 
                  widget = forms.TextInput(
                        attrs = {
                            "placeholder": "Title",
                        }
                    )
                )

#    email       = forms.EmailField(label = '', 
#                  widget = forms.TextInput(
#                        attrs = {
#                            "placeholder": "Email",
#                        }
#                    )
#                )

    description = forms.CharField(label = '',
                        required = False,
                        widget = forms.Textarea(
                            attrs = {
                                "placeholder": "Description",
                                "class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 10,
                                "cols": 60
                            }
                        )
                    )

    price       = forms.DecimalField(label = '',
                        widget = forms.TextInput(
                            attrs = {
                                "placeholder": "Price",
                            }
                        )
                    )

    summary     = forms.CharField(label = '',
                        required = False,
                        widget = forms.Textarea(
                            attrs = {
                                "placeholder": "Summary",
                                "rows": 10,
                                "cols": 60
                            }
                        )
                    )

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        return title 

#    def clean_email(self, *args, **kwargs):
#        email = self.cleaned_data.get("email")
#        return email

class RawProductForm(forms.Form):
    title       = forms.CharField(label = '', 
                  widget = forms.TextInput(
                        attrs = {
                            "placeholder": "Your Title",
                        }
                    )
                )
#    email       = forms.CharField(label = '', 
#                  widget = forms.TextInput(
#                        attrs = {
#                            "placeholder": "Your Email",
#                        }
#                    )
#                )
    description = forms.CharField(label = '',
                        required = False,
                        widget = forms.Textarea(
                            attrs = {
                                "placeholder": "Your Description",
                                "class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 10,
                                "cols": 60
                            }
                        )
                    )
    price       = forms.DecimalField(label = '',
                        widget = forms.Textarea(
                            attrs = {
                                "placeholder": "Your Price",
                                "rows": 1,
                                "cols": 9
                            }
                        )
                    )
    summary     = forms.CharField(label = '',
                        required = False,
                        widget = forms.Textarea(
                            attrs = {
                                "placeholder": "Your Summary",
                            }
                        )
                    )
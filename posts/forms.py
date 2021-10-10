from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ['title','description', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control', 'name':'title','placeholder':'عنوان', 'class':'form-control w-100 mt-3'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'name': 'description', 'placeholder':'توضیحات', 'class':'form-control w-100 mt-3'
            }),
            'picture': forms.FileInput(attrs={
                'class':'form-control btn btn-primary', 'name':'picture', 'class':'form-control w-100 p-2 rounded mt-3'
            })
        }
        labels = {
            'title':'عنوان پستتون:',
            'description':'بدنه پستتون رو هم کامل کنید:',
            'picture':'خب اینجا هم میتونی یه عکس واسه پستت بذاری:)'
        }
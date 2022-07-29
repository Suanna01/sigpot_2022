from django import forms
from .models import FreePost, Comment

class FreePostform(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['body']

        # fields = ['title', 'body']
    
    def __init__(self, *arg, **kwargs):
        super(FreePostform, self).__init__(*arg, **kwargs)

        # self.fields['title'].widget.attrs = {
        #     'class': 'form-control',
        #     'placeholder':"글 제목을 입력해주세요",
        #     'row': 20
        # }
        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder':"글 제목을 입력해주세요",
            'row': 20,
            'cols' : 100
        }


class PostModelForm(forms.ModelForm):
    class Meta:
        model = FreePost
        # fields = ['title', 'body']
        fields = ['body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        # fields = ['title', 'body']

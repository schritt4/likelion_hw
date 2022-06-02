from django import forms
from .models import FreePost, FreeComment

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'body', 'image']
    
    def __init__(self, *args, **kwargs):
        super(FreePostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : '글 제목을 입력해주세요',
            'rows' : 20
        }

        self.fields['body'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : '본문을 입력해주세요',
            'rows' : 20,
            'cols' : 100
        }

class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : '댓글을 입력해주세요',
            'rows' : 10,
            'cols' : 100
        }
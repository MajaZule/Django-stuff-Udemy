from django import forms
from blog.models import Post, Comment



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # connects to Post model
        fields = ('author', 'title', 'text',)
        # this is all we want to edit

        widgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'}),
            # we are connecting Textarea attribute ( a text in a blog post form) to editable class,
            # medium-editor-textarea class and to postcontent class(our own class)
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # connects to Comment model
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs = {'class':'textinputclass'}),
            'text': forms.Textarea(attrs = {'class':'editable medium-editor-textarea'}),
        }

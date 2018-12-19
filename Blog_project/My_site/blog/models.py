from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # we are linkng author to authorised user (superuser)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default= timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # with this we define a publish date which we didn't specify at published_date; we count at the time of publish and not at the time of writing

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
        # get absolute url: after the author posts post/comment, where should the website take them? --> reverse function
        # we use detail views for the post and function views for the comment
        # go to the post_detail page
        # also get_absolute_url name should always be the same - django expects it
        # pk = primary key

    def __str__(self):
        return self.title
        # title makes the most sense to return it as a string



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    # each comment is connected to a blog app post
    author = models.CharField(max_length = 150)
    # author is not the author of the post, is just a john/jane doe typing in their name
    text = models.TextField
    create_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)
    # approved comment here should be the same as is the one at approve_comments func

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
        # post_list is gonna be the homepage

    def __str__(self):
        return self.text

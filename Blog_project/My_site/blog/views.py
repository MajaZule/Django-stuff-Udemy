from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, Listview,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView,)



class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView():
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
        # with get_queryset we are doing sequel query on my model;
        # grab post model, all the objects and filter them by date;
        # lte: grab objects less than or equal to the current time and order them by publish date (- in front means by descending)
        # translating sql code into python


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    # if u want to create a post, u need to be logged in
    login_url = '/login/'
    # if u are not logged in, go to /login page
    redirect_field_name = 'blog/post_detail.html'
    # redirect them to detail view
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    # reverse_lazy: when we delete a post, we want to redirect user to another page;
    # reverse_lazy takes care of it but it waits until the user actually deletes the post;
    # if we didn't incorporate reverse_lazy, user would be immediately redirected, before even deleting a post


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')



# NOW THIS IS FOR THE COMMENTS:

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            # post reffers to post under class Comment in models.py
            comment.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = CommentForm
    return render(request, 'blog/comment_form.html', {'form':form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk = post_pk)
    # here is pk = post_pk because when we delete the comment, it's not gonna remember it's pk;
    # that's why we have to save it first



# RELATED TO THE POST NOW

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish
    return redirect('post_detail', pk = pk)

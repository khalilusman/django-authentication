from django.shortcuts import render , redirect , get_object_or_404
from . models import Post
from django.contrib.auth.decorators import login_required
from .  import forms
from django.http import HttpResponseForbidden

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})





def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_list.html',{'post': post})





@login_required(login_url="/users/login/")
def new_post(request):
    if request.method == 'POST':
       form = forms.CreatePost(request.POST , request.FILES)
       if form.is_valid():
          newpost = form.save(commit=False)
          newpost.author = request.user
          newpost.save()
          return redirect('posts:post')


    else:
     form = forms.CreatePost()
    return render(request, 'new_post.html',{'form' : form} )






@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('posts:post')







@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post')
    else:
        form = forms.CreatePost(instance=post)

    return render(request, 'edit_post.html', {'form': form})





from django.views.generic.edit import DeleteView

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    

    if request.method == 'POST':
        form = DeleteView(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.delete()
            return redirect('posts:post')
    else:
        form = DeleteView(instance=post)

    return render(request, 'post_list.html', {'form': form})



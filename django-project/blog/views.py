from ctypes.wintypes import tagMSG

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from requests import post

from .forms import PostForm
from .models import Post


def home(request , tag=None):
    tag_obj = None
    if not tag:
       posts=Post.objects.all()
    else:
        tag_obj = get_object_or_404(tagMSG , slug=tag)
        posts = Post.objects.filter(tags__in=[tag_obj])
    paginator = Paginator(posts , 5)
    page = request.GET.get('page' , 1)
    posts = paginator.get_page(page)

    return render(request , 'home.html' ,
                {'section' : 'home',
                 'posts': post,
                 })

def detail(request , slug=None):
    post = get_object_or_404(Post , slug=slug)
    return render(request , 'blog/detail.html' , 
                   {
                      'section': 'blog_detail',
                      'post':post,
                   })
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request , 'blog/create.html',{'section': 'blog_create' , 'form' : form}) 
def edit(request , pk=None):
    post = get_object_or_404(Post , pk=pk)
    if request.method == 'post':
        form = PostForm(request.POST ,request.FILES , instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:detail" , slug=post.slug)
        else:
            form = PostForm(instance=post)
        return render(request , 'blog/edit.html' ,
                      {'section' : 'blog_edit' ,
                       'form':form,
                       'post': post,   
                      })    





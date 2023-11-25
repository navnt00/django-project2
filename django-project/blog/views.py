from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post
from .forms import PostForm


def home(request):
    post=Post.objects.all()
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
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            form = PostForm()
        return render(request , 'blog/create.html',{'section': 'blog_create' , 'form' : form,}) 
def edit(request , pk=None):
    post = get_object_or_404(Post , pk=pk)
    if request.method == 'post':
        form = PostForm(request.POST , instance=post)
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





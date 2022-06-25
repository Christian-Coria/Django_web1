from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic import View

from blog.models import Post
from .forms import PostCreateForms
# Create your views here.
class BlogListView(View):
    def get(self,request,*args,**kwargs):
        context = {   

        }
        return render(request,'blog_list.html', context)

class BlogCreateViews(View):
    def get(self,request,*args,**kwargs):
        form=PostCreateForms()
        context = {   
              'form':form
        }
        return render(request,'blog_create.html', context)

    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            form = PostCreateForms(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content= form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title= title ,content=content )
                p.save()
                return redirect('blog:home')

        context = {   


        }
        return render(request,'blog_create.html', context)
        
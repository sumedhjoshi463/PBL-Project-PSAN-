from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView,CreateView, UpdateView,DeleteView
from .models import Category, Post
from theblog.models import Post
from .forms import PostForm , EditForm
from django.http import HttpResponseRedirect


class HomeView(ListView):
     model = Post
     template_name = 'home.html'
     ordering = ['-post_date']

     def get_context_data(self,*args ,**kwargs) :
          cat_menu = Category.objects.all()
          context = super(HomeView,self).get_context_data(*args ,**kwargs)
          context["cat_menu"] = cat_menu
          return context
    
class ArticleDetailView(DetailView) :
     model = Post
     template_name = 'article_details.html'

     def get_context_data(self,*args ,**kwargs) :
          cat_menu = Category.objects.all()
          context = super(ArticleDetailView,self).get_context_data(*args ,**kwargs)
          stuff = get_object_or_404(Post, id=self.kwargs['pk'])
          total_likes= stuff.total_likes()
          liked= False
          if stuff.likes.filter(id=self.request.user.id).exists():
               liked = True
          context["cat_menu"] = cat_menu
          context["total_likes"] = total_likes
          context["liked"]= liked
          return context

class AddCategoryView(CreateView) :
     model = Category
     template_name = 'add_category.html'
     fields = '__all__'

class AddPostView(CreateView) : 
     model = Post
     form_class = PostForm
     template_name = 'add_post.html'
     #fields = '__all__'

class UpdatePostView(UpdateView):
     model = Post
     template_name = 'update_post.html'
     form_class = EditForm
     #fields = ['title','domain','body']

class DeletePostView(DeleteView):
     model = Post
     template_name = 'delete_post.html'
     success_url = reverse_lazy('home')
     #form_class = EditForm
     #fields = ['title','domain','body']


def CategoryView(request, cats):
     category_posts = Post.objects.filter(category= cats)
     return render(request,'categories.html',{'cats':cats,'category_posts':category_posts})    


def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists() :
     post.likes.remove(request.user)
     liked = False
    else: 
     post.likes.add(request.user)#saving likes in table in database
     liked = True


    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
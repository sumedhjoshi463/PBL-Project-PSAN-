
from django.urls import path,include
#from .import views
from django.views import generic
from .views import HomeView, ArticleDetailView,AddPostView,UpdatePostView,DeletePostView, AddCategoryView
from .views import CategoryView, LikeView




urlpatterns = [
      #what int:pk(here pk refers to primary key) will do is it assign numbers to blogs based on thier primary key eg. the first blog will be article/1
     #path('',views.home, name='home')
     path('', HomeView.as_view(), name="home"),
     path('article/<int:pk>/',ArticleDetailView.as_view(), name="article-detail"),
     path('add_post/', AddPostView.as_view(), name="add_post"),
     path('add_category/', AddCategoryView.as_view(), name="add_category"),   
     path('article/edit/<int:pk>' , UpdatePostView.as_view(), name="update_post"), 
     path('article/<int:pk>/delete' ,DeletePostView.as_view(), name="delete_post"),
     path('category/<str:cats>/', CategoryView, name="category"),
     path('like/<int:pk>/',LikeView, name="like_post"),
     
]  

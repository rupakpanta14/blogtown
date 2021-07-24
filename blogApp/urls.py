from django.urls import path
from . import views
from .views import blog, search, CategoryView, blogdetail, PostCreateView


urlpatterns = [
path('', blog.as_view(), name="blog"),
path('search', search, name="search"),
path('create-post', PostCreateView.as_view(), name="create_post"),
path('category/<str:cats>/', CategoryView, name="category"),
path('<slug:slug>/send-comment', views.send_comment, name="send_comment"),
path('<slug:slug>/', blogdetail.as_view(), name="blog-detail"),
]

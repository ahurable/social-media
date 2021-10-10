from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AddPostForm
from .models import Post
from django.views.generic import View, ListView
from django.contrib.messages import success, error
from users.models import CustomUserModel
from django.db.models import Q
# Create your views here.

class AddPostView(View):

    def get(self, request):
        post_form = AddPostForm()
        return render(request, 'posts/add_post.html', {'form':post_form})

    def post(self, request):
        post_form = AddPostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = request.user
            instance.save()
            success(request, 'پست شما با موفقیت به افزوده شد', extra_tags='success')
            return redirect('home_url')

def like(request, id):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            post.likes.add(user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostListView(View):
    def get(self, request):
        search_query = request.GET.get('search')
        if search_query:
            posts = Post.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        else:
            posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts':posts})

class UserPostListView(ListView):

    context_object_name = 'posts'
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        _username = self.kwargs.get('username')
        user = CustomUserModel.objects.get(username=_username)
        queryset = Post.objects.filter(author_id=user.id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['username'] = self.kwargs.get('username')
        return context

class SearchView(View):
    def get(self, searched_item):
        posts = Post.objects.filter(description__exact=searched_item)
        return render(request, 'posts/post_list.html', {'posts': posts})

# def PostListView(request, username):
#
#     user = CustomUserModel.objects.get(username=username)
#     posts = Post.objects.filter(author_id=user.id)
#     return render(request, 'posts/post_list.html', {'posts':posts})

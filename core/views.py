from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post

class HomePage(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        return render(request, 'index.html', {'posts':posts})


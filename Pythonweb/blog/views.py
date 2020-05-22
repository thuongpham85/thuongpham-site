from django.shortcuts import render
from django.http import Http404
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.
#def list(request):
#    Data = {'Posts': Post.objects.all().order_by('-date')}
#    return render(request, 'blog/blog.html', Data)
#def post(request, id):
#    try:
#        post = Post.objects.get(id=id)
#    except Post.DoesNotExist:
#        raise Http404("Bai viet khong ton tai")
#    return render(request, 'blog/post.html', {'post':post})
#class PostListView(ListView):
#    queryset = Post.objects.all().order_by('-date')
#    template_name = 'blog/blog.html'
#    context_object_name = 'Posts'
#    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post": post, "form": form})
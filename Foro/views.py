from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'Foro/index.html', {})

def Registro(request):
    return render(request, 'Foro/Registro.html', {}) 

def Download(request):
    return render(request, 'Foro/Download.html', {}) 

def login(request):
    return render(request, 'registration/login.html', {}) 

def password_reset_form(request):
    return render(request, 'registration/password_reset_form.html', {})

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html', {})

def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html', {})

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html', {})

def Devs(request):
    return render(request, 'Foro/Devs.html', {}) 

def Juego(request):
    return render(request, 'Foro/Juego.html', {})

def Desarrollo(request):
    return render(request, 'Foro/Desarrollo.html', {})  

def permiso(request):
    return render(request, 'Foro/permiso.html', {})  

def foro(request):
    queryset = request.GET.get("buscar")  
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(text__icontains = queryset)
        ).distinct()
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'Foro/foro.html', {'posts': posts })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Foro/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Foro/post_edit.html', {'form': form})

def post_edit(request, pk):
    user = request.user
    if user.has_perm('Foro.user'):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'Foro/post_edit.html', {'form': form})
    else:
        return render(request, 'Foro/permiso.html')

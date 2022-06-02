from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import FreeComment, FreePost
from .forms import FreePostForm, FreeCommentForm

# Create your views here.
def new(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user            
            unfinished.save()
            return redirect('index')
    else:
        form = FreePostForm()
    return render(request, 'new.html', {'form':form})

def detail(request, freepost_id):
    freepost = get_object_or_404(FreePost, pk=freepost_id)
    comment_form = FreeCommentForm()
    return render(request, 'detail.html', {'freepost':freepost, 'comment_form':comment_form})

def index(request):
    freepost_index = FreePost.objects.all().order_by('-date')
    return render(request, 'index.html', {'freepost_index':freepost_index})

def comment(request, freepost_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=freepost_id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('detail', freepost_id)

def update(request, freepost_id):
    freepost = get_object_or_404(FreePost, pk=freepost_id)
    if request.method == 'POST':
        form = FreePostForm(request.POST, instance=freepost)
        if form.is_valid():
            freepost = form.save(commit=False)
            freepost.modify_date = timezone.now()
            freepost.save()
            return redirect('detail', freepost_id)
    else:
        form = FreePostForm(instance=freepost)
    
    return render(request, 'update.html', {'form' : form})

def delete(request, freepost_id):
    freepost = get_object_or_404(FreePost, pk=freepost_id)
    if request.method == 'GET':
        freepost.delete()
    return redirect('index')

def comment_delete(request, comment_id, freepost_id):
    freecomment = get_object_or_404(FreeComment, pk=comment_id)
    if request.method == 'GET':
        freecomment.delete()
    return redirect('detail', freepost_id)
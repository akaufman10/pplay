from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Play, Submission
from .forms import PlayForm, ContactForm
from django.shortcuts import redirect
from django.contrib.auth import logout


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})

def loading(request):
	return render(request, 'blog/loading.html',{})

def about(request):
	return render(request, 'blog/about.html',{})

def thanks(request):
	return render(request, 'blog/thanks.html',{})

def login(request):
	return render(request, 'blog/login.html',{})

def logout(request):
    logout(request)
    return render(request, 'blog/home.html',{})

def contact(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
	    data = form.save(commit=False)
            data.submitted_date = timezone.now()
            data.save()
	    return redirect('thanks')

    else:
        form = ContactForm()
    
    return render(request, 'blog/contact.html', {'form':form})
            

def home(request):
	plays = Play.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/home.html',{'plays':plays})

def play_detail(request,pk):
	play = get_object_or_404(Play,pk=pk)
	return render(request, 'blog/play_detail.html', {'play':play})

def play_new(request):
    if request.user.is_authenticated():
	    if request.method == "POST":
		form = PlayForm(request.POST)
		if form.is_valid():
                    play = form.save(commit=False)
                    play.author = request.user
                    play.logo = request.user.userprofile.icon
                    play.published_date = timezone.now()
                    play.save()
                    return redirect('play_detail', pk=play.pk)
            else:
                form = PlayForm()
            return render(request, 'blog/play_edit.html', {'form': form})
    else:
        return render(request, 'blog/login.html', {})


def play_edit(request, pk):
    play = get_object_or_404(Play, pk=pk)
    user = request.user
    if request.method == "POST":
        form = PlayForm(request.POST, instance=play)
        if form.is_valid():
            play = form.save(commit=False)
            play.author = request.user
            play.logo = request.user.userprofile.icon
            play.published_date = timezone.now()
            play.save()
            return redirect('play_detail', pk=play.pk)
    else:
        form = PlayForm(instance=play)
    return render(request, 'blog/play_edit.html', {'form': form,'user':user})



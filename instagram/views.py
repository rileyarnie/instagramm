from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView, DetailView, View
from .models import Image, Profile
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from decouple import config
# Create your views here.



def home(request):
    return render(request, 'instagram/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'WELCOME!!!'
            message = 'Welcome to Instagram and thank you for signing up. Enjoy!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [form.cleaned_data.get('email')]
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created!! You can now login!')
            send_mail( subject, message, from_email, to_list, fail_silently=True)

            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created! Log In Now!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class ImageListView( LoginRequiredMixin,  ListView):
    model = Image 
    context_object_name = 'images'
    ordering = ['-date_posted']



def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)



# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self,form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


# @login_required
# def UserProfile(request):
    
#     images = Image.objects.all()
    
    
#     return render(request, 'user/user_profile.html', context)

@login_required
def search_results(request):
    if 'user' in request.GET and request.GET['user']:
        search_term = request.GET.get("user")
        searched_profiles = Profile.search_by_username(search_term)
        message= f"{search_term}"
        context = {
            'message': message,
            'searched_profiles': searched_profiles
        }
        return render(request, "instagram/search.html", context)
    else:
        message = 'No users with that name found. Try Again!'
        return render(request, 'instagram/search.html',{"message":message})

    


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['image_post', 'image_caption'] 

    def form_valid(self, form):
        form.instance.image_by = self.request.user
        return super().form_valid(form)



class ImageDetailView(DetailView, FormMixin):
    model = Image
    form_class = CommentForm
    def form_valid(self, form):
        return super().form_valid(form)
    

class ImageDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/'

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.image_by:
            return True
        return False 


@login_required
def homepage(request):
    images = Image.objects.all().order_by('-date_posted')
    is_liked = False
    # if images.likes.filter(id=request.user.id).exists():
    #     is_liked = False

    current_user = request.user

    if request.method == 'POST':
        form = CommentForm(request.POST, auto_id=False)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            # image = Image.objects.get(pk=id)
            image = Image.objects.get(pk=img_id)
            comment.image = image
            comment.save()
        return redirect(f'/#{img_id}',)
    else:
        form = CommentForm(auto_id=False)

        context={
        'form': form,
        'images': images,
        'is_liked': is_liked,
    }
    return render(request, 'instagram/homepage.html', context)


@login_required
def like_image(request):
    image = get_object_or_404(Image, id = request.POST.get('image_id'))
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked = False
    else:
        image.likes.add(request.user)
        is_liked =True

    return HttpResponseRedirect(image.get_absolute_url())


class UserImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'users/user_images.html'
    context_object_name = 'images'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Image.objects.filter(image_by=user).order_by('-date_posted')
       


def testProfile(request):
    
    images = Image.objects.all().order_by('-date_posted')
    

    return render(request, 'instagram/testprofile.html', {"images":images})
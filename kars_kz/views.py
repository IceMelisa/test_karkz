from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Post, CustomUser
from .forms import CustomUserForm, ChangePasswordForm, PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'base.html', {'posts': posts})

def profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "Вы не авторизованы. Пожалуйста, войдите в систему.")
        return redirect('log')   
    user = request.user
    return render(request, 'profile.html', {'user': user})


def logout_view(request):
    logout(request)  
    return redirect('log')  
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            post.save()  
            messages.success(request, 'Пост успешно создан!')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка при создании поста. Пожалуйста, попробуйте снова.')

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['name']
        if username and email and password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Пользователь с таким именем уже существует!')
                return redirect('reg')
            user = CustomUser.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Регистрация прошла успешно!')
                return redirect('index')  
            messages.error(request, 'Не удалось выполнить вход после регистрации.')
            return redirect('log')  
        else:
            messages.error(request, 'Заполните все поля!')
            return redirect('reg')  
    return render(request, 'reg.html')  

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Неверный логин или пароль!')
            return redirect('log') 

    return render(request, 'log.html')  


def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен!")
            return redirect('profile')
        else:
            messages.error(request, "Ошибка при обновлении профиля.")
    else:
        form = CustomUserForm(instance=request.user)  

    return render(request, 'edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, "Пароль успешно изменен!")
            return redirect('profile')
        else:
            messages.error(request, "Ошибка при изменении пароля.")
            print(form.errors)
    else:
        form = ChangePasswordForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})
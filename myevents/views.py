from django.shortcuts import render, redirect
from .models import Category, Event
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('index')

    context = {'form': form, 'page': page}
    return render(request, 'login_register.html', context)


@login_required(login_url='login')
def index(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        events = Event.objects.filter(category__user=user)
    else:
        events = Event.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'events': events}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def viewEvent(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'event.html', {'event': event})


@login_required(login_url='login')
def addEvent(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            event = Event.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('index')

    context = {'categories': categories}
    return render(request, 'add.html', context)
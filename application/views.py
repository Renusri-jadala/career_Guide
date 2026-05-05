from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login ,logout,authenticate
from django.shortcuts import get_object_or_404
from .models import CareerPath, Technology,wish
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        First_Name = request.POST['name']
        Email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmation_password = request.POST['cnfm_password']
        if password == confirmation_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists, please choose a different one.')
                return redirect('register')
            else:
                if User.objects.filter(email=Email).exists():
                    messages.error(request, 'Email already exists, please choose a different one.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=Email,
                        first_name=First_Name,
                    )
                    user.save()
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
        return render(request, 'register.html')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)
            if user.check_password(password):
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'login successfull')
                    return redirect('/')
                else:
                   messages.error(request,'please check the Password Properly')
                   return redirect('login')
            else:
                messages.error(request,"please check the Password Properly")  
                return redirect('login') 
        else:
            messages.error(request,"username doesn't exist")
            return redirect('login')
    return render(request,'login.html')
# Load and preprocess the dataset
def logout_view(request):
    logout(request)
    return redirect('login')


def add_career(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        CareerPath.objects.create(name=name, description=description,image=image)
        return redirect("/")  # Redirect after submission
    return render(request, "addcareer.html")

def add_technology(request):
    careers = CareerPath.objects.all()  
    if request.method == "POST":
        name = request.POST.get("name")
        career_id = request.POST.get("career_path")
        description = request.POST.get("description")
        link = request.POST.get("link")
        career_path = CareerPath.objects.get(id=career_id)
        Technology.objects.create(name=name, career_path=career_path, description=description, link=link)
        
        return redirect("home")
    return render(request, "add_technology.html", {"careers": careers})

def career_list(request):
    careers = CareerPath.objects.all()  # Fetch all career paths
    return render(request, "career.html", {"careers": careers})

def technologies(request, pk):
    career = get_object_or_404(CareerPath, id=pk)  # Fetch a single CareerPath
    technologies = Technology.objects.filter(career_path=career)  # Fetch technologies related to it
    return render(request, "technologies.html", {"career": career, "technologies": technologies})


@csrf_exempt
@login_required
def add_to_wishlist(request, pk):
    if request.method == "POST":
        career = get_object_or_404(CareerPath, id=pk)

        # Toggle wishlist item
        wishlist_item, created = wish.objects.get_or_create(career=career, user=request.user)

        if created:
            messages.success(request, "Career added to wishlist.")
        else:
            messages.success(request, "Career already added to wishlist.")
    return redirect(request.META.get('HTTP_REFERER', 'career_list'))

def wishlist(request):
    wishlist_items = wish.objects.filter(user=request.user)  # Fetch wishlist careers
    return render(request, "wishlist.html", {"wishlist_items": wishlist_items})
def add_wish(request,pk):
    career=CareerPath.objects.get(id=pk)
    s=wish.objects.create(user=request.user,career=career)
    return redirect('career_list')

def remove_item(request,pk):
    id=wish.objects.get(user=request.user,id=pk)
    id.delete()
    return redirect('wishlist')
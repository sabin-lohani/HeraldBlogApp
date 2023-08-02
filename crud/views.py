from django.core.mail import EmailMessage
from projectdemo.settings import EMAIL_HOST_USER #replace root with your project name
from django.template.loader import render_to_string

from django.shortcuts import render, redirect
from .models import Blog, Contacts, User,FooterContent, FooterLink # manager objects
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, MyUserCreationForm
from django.db.models import Q


# Create your views here.
def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    blogs = Blog.objects.filter(
        Q(author__name__icontains = q) |
        Q(author__email__icontains = q) |
        Q(author__username__icontains = q) |
        Q(title__icontains = q) |
        Q(subheading__icontains = q) 
    )
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    blogsFinal = paginator.get_page(page_number)
    return render(request,"crud/index.html",{"blogs": blogsFinal })

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('crud:home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('crud:home')
        
        else:
            messages.error(request, "Username or password does not exist")

    context = {'page': page}
    return render(request,"crud/login-register.html", context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = MyUserCreationForm()
    for field in form:
        print(field.label)
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('crud:home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request,"crud/login-register.html", {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('crud:home')

def about(request):
    return render(request,"crud/about.html")

def partData(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        "blog": blog
    }
    return render(request, "crud/post.html", context)

@login_required(login_url = "crud:login")
def createBlog(request):
    if(request.method == 'POST'):
        Blog.objects.create(
            author = request.user,
            title = request.POST.get('title'),
            subheading = request.POST.get('subheading'),
            description = request.POST.get('description')
        )
        return redirect('crud:home')
    return render(request, "crud/create-blog.html")

@login_required(login_url = "crud:login")
def edit(request, id):
    blog = Blog.objects.get(id = id)
    form = BlogForm(request.POST or None, instance=blog)

    if(request.method == 'POST'):
        form = BlogForm(request.POST, instance=blog)
        if(form.is_valid()):
            form.save()
            return redirect('crud:home')
    
    return render(request, "crud/edit.html", {"form": form, 'id': id})

@login_required(login_url = "crud:login")
def delete(request, id):
    blog = Blog.objects.get(id = id)

    if(request.method == 'POST'):
        blog.delete()
        return redirect('crud:home') 
    
    return render(request, 'crud/confirmdelete.html', {'obj': blog})    

def contacts(request):
    if(request.method == "POST"):
        dataName = request.POST.get("name")
        dataEmail = request.POST.get("email")
        dataSubject = request.POST.get("subject")
        dataMessage = request.POST.get("message")
        template = render_to_string('crud/email.html',{'name':dataName,'description':dataMessage,'mail':dataEmail})
        recipient = EMAIL_HOST_USER,

        email = EmailMessage(dataSubject,template,EMAIL_HOST_USER,recipient)

        email.fail_silently=False
        if email!=None:
            email.send()


        # contacts = Contacts.objects.create(
        #     name = dataName,
        #     email = dataEmail,
        #     message = dataMessage
        # )

        return redirect('crud:home')

    return render(request, "crud/contact.html")
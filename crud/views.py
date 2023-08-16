from django.core.mail import EmailMessage
from projectdemo.settings import EMAIL_HOST_USER #replace root with your project name
from django.template.loader import render_to_string

from django.shortcuts import render, redirect
from .models import Blog # manager objects
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.db.models import Q
from django.template import RequestContext


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

def about(request):
    return render(request,"crud/about.html")

def partData(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        "blog": blog
    }
    return render(request, "crud/post.html", context)

@login_required(login_url = "users:login")
def createBlog(request):
    if(request.method == 'POST'):
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('crud:home')
        # Blog.objects.create(
        #     author = request.user,
        #     title = request.POST.get('title'),
        #     subheading = request.POST.get('subheading'),
        #     description = request.POST.get('description')
        # )
    else:
        form = BlogForm()
    return render('crud/create-blog.html', {'form': form},  context_instance=RequestContext(request))

@login_required(login_url = "users:login")
def edit(request, id):
    blog = Blog.objects.get(id = id)
    form = BlogForm(request.POST or None, instance=blog)

    if(request.method == 'POST'):
        form = BlogForm(request.POST, instance=blog)
        if(form.is_valid()):
            form.save()
            return redirect('crud:home')
    
    return render("crud/edit.html", {"form": form, 'id': id}, context_instance=RequestContext(request))

@login_required(login_url = "users:login")
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
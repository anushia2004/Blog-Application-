from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Student, Blog
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, BlogForm

def home(request):
    return render(request, "hello/home.html")
              
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            # messages.success(request,"you are now logged in")
            return redirect("home")

        else:
            messages.error(request,"invalid username or password")

    return render(request,"hello/login.html") 

def logout_view(request):
    logout(request)
    return redirect("login")

def student_list(request):
    student = Student.objects.all()
    return render(request,"hello/student_list.html", {"students":student})

def blog_list(request):
    blogs = Blog.objects.all().order_by("created_at")
    return render(request,"hello/blog_list.html", {"blogs":blogs})

@login_required
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, "hello/my_blogs.html",{"blogs":blogs}) 
   
@login_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect("my_blogs")
    else:
        form = BlogForm()
    return render(request, 'hello/blog_form.html',{'form':form}) 

@login_required
def blog_edit(request,pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('my_blogs') 
    else:     
        form = BlogForm(instance=blog)
    return render(request, 'hello/blog_form.html', {'form':form})
    
    
@login_required
def blog_delete(request,pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect("my_blogs")
    return render(request, 'hello/blog_confirm_delete.html', {'blog':blog})
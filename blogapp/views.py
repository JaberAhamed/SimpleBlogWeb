
from django.shortcuts import render, get_object_or_404, redirect,Http404
from .models import articla,author,catagory,comment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .form import creatForm, registerForm, authorForm,commentform,createCatagory
from django.contrib import messages

def indexView(request):

   article = articla.objects.all()

   search = request.GET.get('q')
   if search:
       article = article.filter(Q(title__icontains=search)|Q(body_incontains=search))
   paginator = Paginator(article, 8)  # Show 25 contacts per page

   page = request.GET.get('page')
   contacts = paginator.get_page(page)

   context = {
       "article":contacts,

   }
   return render(request, 'index.html', context=context)


def profileView(request, name):
    author_name = get_object_or_404(User, username=name)
    auth = get_object_or_404(author, name=author_name.id)
    author_post = articla.objects.filter(artical_author=auth)



    context={
        'auth': auth,
        'auth_post': author_post,

    }

    return render(request, 'profile.html', context=context)


def singleView(request, id):

    post = get_object_or_404(articla, pk=id)
    first= articla.objects.first()
    last = articla.objects.last()
    related = articla.objects.filter(catagory = post.catagory).exclude(id=id)[:4]
    paginator = Paginator(related, 2)  # Show 25 contacts per page

    post_comment =  comment.objects.filter(post = id)

    form  = commentform(request.POST or None)
    instance = form.save(commit=False)
    instance.post=post
    instance.save()

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        "post": post,
        "fast": first,
        "last": last,
        "rel":contacts,
        "form":form,
        "post_comment":post_comment
    }
    return render(request, 'single.html', context=context)

def topicView(request, name):

    cat = get_object_or_404(catagory, name=name)
    post=articla.objects.filter(catagory = cat.id)
    paginator = Paginator(post, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    contex = {

        "catagory": cat,
        "post": contacts,
    }
    return render(request, 'catagory.html', context=contex)



def loginView(request):

     if request.user.is_authenticated:
         return redirect('blog:index')
     else:
         if request.method == "POST":
             user = request.POST.get('user')
             password = request.POST.get('password')
             auth = authenticate(username=user, password=password)
             if auth is not None:
                 login(request, auth)
                 messages.success(request, 'Log in Success')
                 return redirect('blog:index')
             else:
                 messages.error(request, messages.INFO, 'Log in Failed')
                 return redirect('blog:login')
     return render(request, 'login.html')

def getlogoutView(request):
    logout(request)
    return redirect('blog:index')

def fromView(request):

 if request.user.is_authenticated:
    user = get_object_or_404(User, id= request.user.id)
    auth_profile = author.objects.filter(name=user.id)

    if auth_profile:
        u=get_object_or_404(author, name=user)
        form = creatForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            intance = form.save(commit=False)
            intance.artical_author = u
            intance.save();
            return redirect('blog:index')
        else:
            return redirect('blog:login')
        return render(request, 'create.html', {"form": form})
    else:
        formauthor = authorForm(request.POST or None, request.FILES or None)
        if formauthor.is_valid():
            instance = formauthor.save(commit=False)
            instance.name=user
            instance.save();
            return redirect('profile')
        return render(request, 'authorregister.html', {"form": formauthor})






 else:
     redirect('blog:login')




def authprofileView (request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id= request.user.id)
        auth_profile = author.objects.filter(name=user)


        if auth_profile:
            auth = get_object_or_404(author, name=user)
            post = articla.objects.filter(artical_author=auth.id)
            return render(request, 'authinfo.html', {"post": post, "auth":auth})
        else:
            form = authorForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance= form.save(commit=False)
                instance.name=user
                instance.save();
                return redirect('profile')

            return render(request, 'authorregister.html', {"form":form, })
    else:
        return  redirect('blog:login')




def postupdateView(request,pid):

    if request.user.is_authenticated:
     u = get_object_or_404(author, name=request.user.id)
     post = get_object_or_404(articla, id = pid)
     form = creatForm(request.POST or None, request.FILES or None, instance  = post)
     if form.is_valid():
        intance = form.save(commit=False)
        intance.artical_author=u
        intance.save();
        messages.success(request, 'update success ')
        return redirect('blog:profile')
    else:
        return redirect('blog:login')
    return render(request, 'create.html', {"form":form})


def deleteView(request,pid):

    if request.user.is_authenticated:
        post = get_object_or_404(articla, id=pid)
        post.delete()
        return  redirect('blog:profile')
    else:
       return render(request, 'blog:login')

def registerView(request):

    form = registerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save();
        return redirect('blog:login')
    return render(request, 'register.html', {"form":form})

def showCatagoryView(request):

    all_catagory=catagory.objects.all()


    return render(request, "showcatagory.html", {"catagory":all_catagory})

def createCatagoryView(request):

    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            form = createCatagory(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('blog:catagory')
            return render(request, "createCatagory.html", {"form": form})
        else:
            raise Http404("YOU ARE NOT SUPER USER OR Admin")


def cataUpdate(request, name):

    cata=get_object_or_404(catagory, name=name)
    form = createCatagory(request.POST or None, instance = cata)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return redirect('blog:catagory')

    return render(request, "createCatagory.html", {"form": form})


def deleteCatagory(request, name):

    cata=catagory.objects.filter(name=name)
    cata.delete()
    return redirect('blog:catagory')
















































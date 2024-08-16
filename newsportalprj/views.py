from django.db.models import Count
from django.contrib.auth import authenticate, login as auth_login,logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

from newsapp.models import Category, Comments, Customeuser, News, Subcategory
User=get_user_model

def base(request):
    return render(request,'base.html')

def base1(request):
    return render(request,'base1.html')

def index(request):
    category=Category.objects.all()
    news= News.objects.filter(status='Active').order_by('-id')[:3]
    news1=News.objects.filter(status='Active').order_by('-id')[:4]
    recentnews =  News.objects.filter(status='Active').order_by('-id')[:5]

    print(news)
    context={
        'category':category,
        'news':news,
        'news1':news1,
        'recent':recentnews
    }
    return render(request,'index.html',context)

def login(request):
    return render(request,'login.html')


def singlenews(request,id):
    news=News.objects.get(id=id)
    category=Category.objects.all()
    recent = News.objects.order_by('-news_post_date')[:4]
    comment=Comments.objects.filter(news_id=news, status='Approved')
    category_counts = Category.objects.annotate(news_count=Count('news'))
    context={
        'news':news,
        'cat_count':category_counts,
        'recent':recent,
        'category':category,
        'com':comment
    }
    return render(request,'single_news.html',context)

def category_details(request,id):
    catid=Category.objects.get(id=id)
    category=Category.objects.all()
    new=News.objects.filter(cat_id=catid,status='Active').order_by('-id')
    paginator = Paginator(new, 4)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    context={
        'catid':catid,
        'news':news,
        'category':category
    }

    return render(request, 'categorywise_news.html', context)


def loginfunction(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            user_type=user.user_type
            if user_type == '1':
                return redirect('dashboard')
            elif user_type == '2':
                return redirect('dashboard')
        else:
            messages.error(request, 'Email or Password is invalid')
            return render(request,'login.html')

            
def Dashboard(request):
    cat_count=Category.objects.all().count()
    sub_count=Subcategory.objects.all().count()
    news_count=News.objects.all().count()
    subadmin_count=Customeuser.objects.all().count()
    context={
        'cat_c':cat_count,
        'sub_c':sub_count,
        'new_c':news_count,
        'subad_c':subadmin_count
    }
    return render(request,'dashboard.html',context)

def signout(request):
    logout(request)
    return redirect('login')


def comment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        postid=request.POST.get('post_id')
        name=request.POST.get('name')
        email=request.POST.get('email')


        news=News.objects.get(id=postid)
        com=Comments(
           news_id=news,
           comment=comment,
           name=name,
           email=email
        )
        com.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

def about(request):
    category=Category.objects.all()
    context={
        'category':category,
    }
    return render(request,'about.html',context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from newsapp.models import Category, Comments,Subcategory,News,Customeuser
from django.shortcuts import redirect, render

@login_required(login_url = 'index')
def addcatpage(request):
    if request.method=='POST':
        catname=request.POST.get('catname')
        catdes=request.POST.get('catdes')
        cat=Category(category_description=catdes,category_name=catname)
        cat.save()
        messages.success(request,'Category add successfully')
        return redirect('addcat')
    return render(request,'admin/categoryadd.html')

@login_required(login_url = 'index')
def viewcategory(request):
    category=Category.objects.all()
    paginator = Paginator(category, 10)
    page_number = request.GET.get('page')
    try:
        cat = paginator.page(page_number)
    except PageNotAnInteger:
        cat = paginator.page(1)
    except EmptyPage:
        cat = paginator.page(paginator.num_pages)
    context={
        'cat':cat
    }
    return render(request,'admin/view_category.html',context)

@login_required(login_url = 'index')
def editcategory(request,id):
    category=Category.objects.get(id=id)
    context={
        'cat':category
    }
    return render(request,'admin/updatecategory.html',context)

@login_required(login_url = 'index')
def updatecategory(request):
    if request.method=='POST':
        catname=request.POST.get('catname')
        id=request.POST.get('cat_id')
        catdes=request.POST.get('cat_des')
        category=Category.objects.get(id=id)
        category.category_name=catname
        category.category_description=catdes
        category.save()
        messages.success(request,'your category details updated successfully')
        return redirect('viewcategory')
    return render(request,'admin/updatecategory.html')

@login_required(login_url = 'index')
def deletecategory(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    messages.success(request,'Record delete successfully')
    return redirect('viewcategory')


@login_required(login_url = 'index')
def addsubpage(request):
    if request.method=='POST':
        catid=request.POST.get('cat_id')
        subcat=request.POST.get('subcatname')
        category=Category.objects.get(id=catid)
        subcat=Subcategory(cat_id=category,sub_category_name=subcat)
        subcat.save()
        messages.success(request,'sub category add successfully')
        return redirect('addsub')
    cat=Category.objects.all()
    context={
        'cat':cat
    }
    return render(request,'admin/subcategoryadd.html',context)

@login_required(login_url = 'index')
def viewsubcat(request):
    subcategory=Subcategory.objects.all()
    paginator = Paginator(subcategory, 10)
    page_number = request.GET.get('page')
    try:
        cat = paginator.page(page_number)
    except PageNotAnInteger:
        cat = paginator.page(1)
    except EmptyPage:
        cat = paginator.page(paginator.num_pages)
    context={
        'cat':cat
    }
    return render(request,'admin/view_subcategory.html',context)

@login_required(login_url = 'index')
def editsubcategory(request,id):
    category=Category.objects.all()
    sub=Subcategory.objects.get(id=id)
    context={
        'cat':category,
        'sub':sub
    }
    return render(request,'admin/updatesubcategory.html',context)

@login_required(login_url = 'index')
def updatesubcategory(request):
    if request.method=='POST':
        subcatname=request.POST.get('subcatname')
        catid=request.POST.get('cat_id')
        subcatid=request.POST.get('subcat_id')

        subcat=Subcategory.objects.get(id=subcatid)
        categoryid=Category.objects.get(id=catid)
        subcat.cat_id=categoryid
        subcat.sub_category_name=subcatname
        subcat.save()
        messages.success(request,'your subcategory details updated successfully')
        return redirect('viewsubcat')
    return render(request,'admin/updatesubcategory.html')

@login_required(login_url = 'index')
def deletesubcategory(request,id):
    cat=Subcategory.objects.get(id=id)
    cat.delete()
    messages.success(request,'Record delete successfully')
    return redirect('viewsubcat')



@login_required(login_url = 'index')
def addnews(request):
    if request.method=='POST':
        catid=request.POST.get('cat_id')
        subcatid=request.POST.get('subcategory_id')
        title=request.POST.get('posttitle')
        details=request.POST.get('postdetails')
        status=request.POST.get('status')
        image=request.FILES.get('postimage')

        category=Category.objects.get(id=catid)
        subcat=Subcategory.objects.get(id=subcatid)
        news=News(
            cat_id=category,
            sub_id=subcat,
            newstitle=title,
            newsdetails=details,
            newsimage=image,
            status=status

        )
        news.save()
        messages.success(request,'news add successfully')
        return redirect('addnews')
    cat=Category.objects.all()
    sub=Subcategory.objects.all()
    context={
        'cat':cat,
        'sub':sub
    }
    return render(request,'admin/newsadd.html',context)

@login_required(login_url = 'index')
def get_subcat(request):
    if request.method=='GET':
        catid=request.GET.get('c_id')
        subcat=Subcategory.objects.filter(cat_id=catid)
        subcat_options = ''
        for subcategory in subcat:
            subcat_options += f'<option value="{subcategory.id}">{subcategory.sub_category_name}</option>'
        return JsonResponse({'subcat_options': subcat_options})

@login_required(login_url = 'index')
def viewnews(request):
    news=News.objects.all().order_by('-id')
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    try:
        newss = paginator.page(page_number)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        newss = paginator.page(paginator.num_pages)
    context={
        'news':newss
    }
    return render(request,'admin/view_news.html',context)

@login_required(login_url = 'index')
def view_newsdetails(request,id):
    category=Category.objects.all()
    news=News.objects.get(id=id)
    context={
        'cat':category,
        'news':news
    }
    return render(request,'admin/updatenews.html',context)

@login_required(login_url = 'index')
def editnews(request,id):
    category=Category.objects.all()
    news=News.objects.get(id=id)
    context={
        'cat':category,
        'news':news
    }
    return render(request,'admin/updatenews.html',context)

@login_required(login_url = 'index')
def updatesnews(request):
    if request.method=='POST':
        catid=request.POST.get('catid')
        subcatid=request.POST.get('subcatid')
        newsid=request.POST.get('newsid')
        title=request.POST.get('newstitle')
        details=request.POST.get('newsdetails')
        status=request.POST.get('status')
        image=request.FILES.get('newsimage')
        try:

            category=Category.objects.get(id=catid)
            subcat=Subcategory.objects.get(id=subcatid)
            news=News.objects.get(id=newsid)

            news.cat_id=category
            news.sub_id=subcat
            news.newsdetails=details
            news.newstitle=title
            news.status=status
            if image:
                news.newsimage=image
            news.save()
            messages.success(request,'news details has been updated successfully')
            return redirect('viewnews')
        except (Subcategory.DoesNotExist, Category.DoesNotExist, News.DoesNotExist):
            messages.error(request,'invalid id provided')
            return redirect('updatenews')
    return render(request,'admin/updatesubcategory.html')

@login_required(login_url = 'index')
def deletenews(request,id):
    news=News.objects.get(id=id)
    news.delete()
    messages.success(request,'Record delete successfully')
    return redirect('viewnews')

@login_required(login_url = 'index')
def commentviews(request):
    comment=Comments.objects.all()
    paginator = Paginator(comment, 10)  

    page_number = request.GET.get('page')
    try:
        comment = paginator.page(page_number)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    context={
        'comm':comment
    }
    return render(request,'admin/comments.html',context)

@login_required(login_url = 'index')
def viewcomment(request,id):
    comment=Comments.objects.filter(id=id)
    context={
        'com':comment
    }
    return render(request,'admin/viewcomment.html',context)

@login_required(login_url = 'index')
def changecommentstatus(request):
    if request.method=='POST':
        id=request.POST.get('comm_id')
        status=request.POST.get('status')
        comment=Comments.objects.get(id=id)
        comment.status=status
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
@login_required(login_url = 'index')
def commentdelete(request,id):
    comment=Comments.objects.get(id=id)
    comment.delete()
    messages.success(request,'comment delete successfully')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url = 'index')
def approvedcomments(request):
    comment=Comments.objects.filter(status='Approved')
    paginator = Paginator(comment, 10)  

    page_number = request.GET.get('page')
    try:
        comment = paginator.page(page_number)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    context={
        'comm':comment
    }
    return render(request,'admin/approvedcomments.html',context)

@login_required(login_url = 'index')
def unapprovedcomments(request):
    comment=Comments.objects.filter(status='Unapproved')
    paginator = Paginator(comment, 10)  

    page_number = request.GET.get('page')
    try:
        comment = paginator.page(page_number)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    context={
        'comm':comment
    }
    return render(request,'admin/unapprovedcomments.html',context)


@login_required(login_url = 'index')
def addsubadmin(request):
    return render(request,'admin/addsubadmin.html')

@login_required(login_url = 'index')
def subadminadd(request):
    if request.method=='POST':
        pic=request.FILES.get('profile_pic')
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        
        if Customeuser.objects.filter(email=email).exists():
            messages.error(request,'Email already exist')
            return redirect('addsubadmin')
        if Customeuser.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
            return redirect('addsubadmin')
        else:
            user=Customeuser(
               first_name=fname,
               last_name=lname,
               username=username,
               email=email,
               user_type=2,
               profile_pic = pic,
            )
            user.set_password(password)
            user.save()            
                       
            messages.success(request,'Sub admin added Successfully')
            return redirect('addsubadmin')

@login_required(login_url = 'index')
def viewsubadmin(request):
    subadmin=Customeuser.objects.filter(user_type=2)
    paginator = Paginator(subadmin, 10)  

    page_number = request.GET.get('page')
    try:
        subadmin = paginator.page(page_number)
    except PageNotAnInteger:
        subadmin = paginator.page(1)
    except EmptyPage:
        subadmin = paginator.page(paginator.num_pages)
    context={
        'subad':subadmin
    }
    return render(request,'admin/viewsubadmin.html',context)

@login_required(login_url = 'index')
def editsubadmin(request,id):
    subadmin=Customeuser.objects.get(id=id)
    context={
        'subadmin':subadmin
    }
    return render(request,'admin/editsubadmin.html',context)

@login_required(login_url = 'index')
def updatesubadmin(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        email=request.POST.get('email')
        uname=request.POST.get('username')
        userid=request.POST.get('userid')
        pic=request.FILES.get('profile_pic')

        user=Customeuser.objects.get(id=userid)
        user.first_name=fname
        user.last_name=lname
        user.email=email
        user.username=uname

        if pic:
            user.profile_pic=pic
        user.save()
        messages.success(request,'profile updated successfully')
        return redirect('viewsubadmin')
    return redirect('editsubadmin')

@login_required(login_url = 'index')
def deletesubadmin(request,id):
    user=Customeuser.objects.get(id=id)
    user.delete()
    messages.success(request,'sub admin delete successfully')
    return redirect('viewsubadmin')

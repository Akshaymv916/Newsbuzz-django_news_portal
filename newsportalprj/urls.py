
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from newsportalprj import adminviews,views

adminviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.base,name='base'),
    path('base1',views.base1,name='base1'),
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('singlenews/<int:id>/',views.singlenews,name='singlenews'),
    path('category_details/<int:id>',views.category_details,name='category_details'),
    path('loginfn',views.loginfunction,name='loginfn'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('signout',views.signout,name='signout'),
    path('comment',views.comment,name='comment'),
    path('about',views.about,name='about'),


    path('addcat',adminviews.addcatpage,name='addcat'),
    path('viewcategory',adminviews.viewcategory,name='viewcategory'),
    path('editcategory/<int:id>/',adminviews.editcategory,name='editcategory'),
    path('updatecategory',adminviews.updatecategory,name='updatecategory'),
    path('deletecategory/<int:id>/',adminviews.deletecategory,name='deletecategory'),

    path('addsub',adminviews.addsubpage,name='addsub'),
    path('viewsubcat',adminviews.viewsubcat,name='viewsubcat'),
    path('editsubcat/<int:id>/',adminviews.editsubcategory,name='editsubcat'),
    path('updatesubcategory',adminviews.updatesubcategory,name='updatesubcategory'),
    path('deletesubcategory/<int:id>/',adminviews.deletesubcategory,name='deletesubcategory'),

    path('addnews',adminviews.addnews,name='addnews'),
    path('viewnews',adminviews.viewnews,name='viewnews'),
    path('editnews/<int:id>/',adminviews.editnews,name='editnews'),
    path('updatenews',adminviews.updatesnews,name='updatenews'),
    path('deletenews/<int:id>/',adminviews.deletenews,name='deletenews'),
    path('get_subcat/', adminviews.get_subcat, name='get_subcat'),
    path('commentsview',adminviews.commentviews,name='commentsview'),
    path('viewcomment/<int:id>/',adminviews.viewcomment,name='viewcomment'),
    path('view_newsdetails/<int:id>/',adminviews.view_newsdetails,name='view_newsdetails'),
    path('changecommentstatus',adminviews.changecommentstatus,name='changecommentstatus'),
    path('commentdelete/<int:id>/',adminviews.commentdelete,name='commentdelete'),

    path('approvedcomments',adminviews.approvedcomments,name='approvedcomments'),
    path('unapprovedcomments',adminviews.unapprovedcomments,name='unapprovedcomments'),

    path('addsubadmin',adminviews.addsubadmin,name='addsubadmin'),
    path('subadminadd',adminviews.subadminadd,name='subadminadd'),
    path('viewsubadmin',adminviews.viewsubadmin,name='viewsubadmin'),
    path('editsubadmin/<int:id>/',adminviews.editsubadmin,name='editsubadmin'),
    path('updatesubadmin',adminviews.updatesubadmin,name='updatesubadmin'),
    path('deletesubadmin/<int:id>/',adminviews.deletesubadmin,name='deletesubadmin')

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

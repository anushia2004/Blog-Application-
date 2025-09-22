    
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name="home"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path('students/',views.student_list, name="student_list"),


    path('blogs/',views.blog_list,name="blog_list"),
    path('blogs/mine/',views.my_blogs,name="my_blogs"),
    path('blogs/create/',views.blog_create,name="blog_create"),
    path('blogs/edit/<int:pk>',views.blog_edit,name="blog_edit"),
    path('blogs/delete/<int:pk>',views.blog_delete,name="blog_delete"),

]
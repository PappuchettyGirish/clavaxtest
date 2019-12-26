from django.conf.urls import url,include
from myapp import views as my_views
from django.urls import path

urlpatterns =[
        url('^$',my_views.index,name='index'),
        url('^signup',my_views.signup,name='signup'),
        url('^login',my_views.login,name='login'),
        url('^user',my_views.user,name='user'),
        url('^logout',my_views.logout,name='logout'),
        path('member-list/',my_views.MemberList.as_view()),
        ]

from django.urls import path
from myapp import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    path('doc/',views.doc,name='doc'),
    path('cont/',views.cont,name='cont'),
    path('dept/',views.dept,name='dept'),
    path('fake/',views.fake,name='fake'),
    path('ap/',views.ap,name='ap'),
    path('ad/',views.ad,name='ad'),


]
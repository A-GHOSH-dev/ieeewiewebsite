from django.contrib import admin
from django.urls import path, include
from ieeewie import views

admin.site.site_header ="IEEE WIE"
admin.site.site_title= "Welcome to my dashboard"
admin.site.index_title="Welcome to my portal"

urlpatterns = [
    
    path('', views.index, name='index'),
    path('newsletters', views.newsletters, name='newsletters'),
    path('newsletteredition', views.newsletteredition, name='newsletteredition'),
    path('newsletterform', views.newsletterform, name='newsletterform'),
    path('blogs', views.blogs, name='blogs'),
    path('page404', views.page404, name='page404'),
    path('registrationclosed', views.registrationclosed, name='registrationclosed'),
    #path('finalreportpdf/<str:pk>', views.finalreportpdf, name='finalreportpdf'),


]
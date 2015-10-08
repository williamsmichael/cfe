from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'trydjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # understanding views
    #-----------------------
    # a user puts in a url to 'request a response'
    # django tries to match the url pattern in urls.py
    # if found (and code works), 
    # then it goes to whatever the setting is after regex
    # regex, {app}.{views.py}.{function}, ..
    # views then RETURNs something

    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#import admin from django contrib file
from django.contrib import admin
#import inclue and path patters for urls 
from django.urls import include, path

urlpatterns = [
	#include allos referenncing to other urlconfs
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


# The idea behind include() is to make it easy to plug-and-play URLs. 
# Since polls are in their own URLconf (polls/urls.py), they can be 
# placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, 
# or any other path root, and the app will still work

# You should always use include() when you include other URL patterns. 
# admin.site.urls is the only exception to this.

# PATH FUNCTION

# The path() function is passed four arguments, two required: route and 
# view, and two optional: kwargs, and name. At this point, it’s worth 
# reviewing what these arguments are for

# PATH ARGUEMENT ROUTE

# route is a string that contains a URL pattern. When processing a request, 
# Django starts at the first pattern in urlpatterns and makes its way down 
# the list, comparing the requested URL against each pattern until it finds 
# one that matches.

# PATH ARGUEMENT KWARGS

# Arbitrary keyword arguments can be passed in a dictionary to the target view. 
# We aren’t going to use this feature of Django in the tutorial. 

# PATH ARGUEMENT NAME

# Naming your URL lets you refer to it unambiguously from elsewhere in Django, 
# especially from within templates. This powerful feature allows you to make 
# global changes to the URL patterns of your project while only touching a single file.
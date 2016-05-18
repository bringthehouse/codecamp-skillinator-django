"""skillinator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import skillsmatrix.views
import skillsmatrix.homework

from skillsmatrix.view.generic import *
from skillsmatrix.view.model import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # For tutorial
    url(r'^myskills/', skillsmatrix.views.MySkills),
    url(r'^homepage/', skillsmatrix.views.HomePage),

    # Give access to some of the views for the testing/code coverage homework
    url(r'^problemthree/', skillsmatrix.homework.ProblemThree),


    url(r'^$', UserRedirectView.as_view(), name="user-redirect-view"),

    url(r'^home/', HomeTemplateView.as_view(), name="home-view"),
    url(r'^home-login/', login_required(HomeTemplateView.as_view()), name="home-login-view"),

    url(r'^model/(?P<pk>[0-9]+)/update/', DeveloperUpdateView.as_view(), name="developer-update-view"),
    
    url(r'^model/(?P<pk>[0-9]+)/', DeveloperDetailView.as_view(), name="developer-detail-view"),
    url(r'^model/', DeveloperListView.as_view(), name="developer-list-view"),

    url(r'^skill/create/', SkillCreateView.as_view(), name="skill-create-view"),
    url(r'^skill/', SkillListView.as_view(), name="skill-list-view"),




]

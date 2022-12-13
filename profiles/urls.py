from django.urls import path

from .views import indexPageView
from .views import aboutPageView
from .views import displayPageView
from .views import inputPageView
from .views import searchPageView
# from .views import inputProfilePageView
from .views import searchProfilePageView
from .views import findSkillsPageView, searchSkillsView
from .views import loginPageView, signin, signout, profilePageView, storeProfilePageView
from .views import addSkill, addSkillSubmit, addNewSkillSubmit, deleteSkillSubmit


urlpatterns = [
    path("", indexPageView, name="index"),    

    path("about", aboutPageView, name="about"),   

    path("display/", displayPageView, name="display"),  

    path("input", inputPageView, name="input"), 

    path("search", searchPageView, name="search"),
    path("searchprofile/", searchProfilePageView, name="searchprofile"),

    path("searchskills", searchSkillsView, name="searchskills"),
    path("findskills/", findSkillsPageView, name="findskills"),

    path('login/', loginPageView, name='login'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),

    path('profile', profilePageView, name='profile'),
    path('storeprofile', storeProfilePageView, name='storeprofile'),
    path('editprofile', storeProfilePageView, name='editprofile'),
    path('addskill', addSkill, name='addskill'),
    path('skillsubmit/', addSkillSubmit, name='skillsubmit'),
    path('newskillsubmit/', addNewSkillSubmit, name='newskillsubmit'),
    path('deleteskill/', deleteSkillSubmit, name='deleteskill'),
    

    

]   


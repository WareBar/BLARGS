from django.urls import path
from . import views

#app_name is the variable for easy calling of url based on the name of the url 
app_name = "POST"

urlpatterns = [
    path("list/", views.post_list, name="list"),
    path("create/", views.post_new, name="new"),
    # slug is the parameter passed to this views.post_page
    path("<slug:slug>", views.post_page, name="page")
]

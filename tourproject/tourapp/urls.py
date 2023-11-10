
from . import views
from django .urls import path

urlpatterns = [

#first path is for home page
    path('',views.demo,name='demo'),

]



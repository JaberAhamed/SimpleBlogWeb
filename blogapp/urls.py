
from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('', views.indexView, name='index'),
    path('author/<name>', views.profileView, name='author'),
    path('artcle/<int:id>', views.singleView, name='artcle'),
    path('topic/<name>', views.topicView, name='topic'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.getlogoutView, name='logout'),
    path('create/', views.fromView, name='create'),
    path('profile/', views.authprofileView, name='profile'),
    path('update/<int:pid>', views.postupdateView, name='update'),
    path('delete/<int:pid>', views.deleteView, name='delete'),
    path('register/', views.registerView, name='register'),
    path('catagoy/', views.showCatagoryView, name='catagory'),
    path('createcatagory/topic', views.createCatagoryView, name='createcatagory'),
    path('catagiryUpdate/<name>', views.cataUpdate, name='cataUpdate'),
    path ('deletecatagory/<name>', views.deleteCatagory, name='deleteCatagory')


]


